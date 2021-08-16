import os
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from func_timeout import func_timeout, FunctionTimedOut
from tqdm import tqdm

from image_fetcher.tools import escape_image_name, download_url


def download_image_with_timeout(url: str, timeout: int, output_directory: str):
    """
    Downloads image from given URL. Will exit if not complete within timeout seconds. Doesn't validate input params.

    Parameters:
    url (str): URL to try and download image from
    timeout (int): seconds to wait for function to execute
    output_directory (str): output_directory to save image to

    Returns:
    bool: whether image was downloaded before timeout
    """
    try:
        func_timeout(
            timeout,
            download_image,
            args=(
                url,
                output_directory,
            ),
        )
        return True
    except FunctionTimedOut:
        return False


def download_image(url: str, output_directory: str):
    """
    Downloads image from given URL.

    Parameters:
    url (str): URL to try and download image from
    output_directory (str): output_directory to save image to
    """
    image_name = escape_image_name(url)
    data = download_url(url)
    with open(os.path.join(output_directory, image_name), "wb") as output_file:
        output_file.write(data)


def multi_thread_image_download(
    urls: str,
    output_directory: str,
    max_fetching_threads=None,
    download_timeout=5,
    verbose=True,
):
    """
    Downloads list of images using multiple threads.

    Parameters:
    url_file_path (list/str): list of URLs or path to text file containing list of URLs
    output_directory (str): destination directory path
    max_image_fetching_threads (int): maximum number of concurrent image download threads (default is cores * 5)
    image_download_timeout (int): maximum wait time in seconds for an image download (default is 5)
    verbose (bool): show tqdm progress bar (default true)

    Returns:
    int: total files in the directory
    """
    # If urls is not a list is must be a path to a file with a list of urls
    if isinstance(urls, str):
        with open(urls, "r") as url_file:
            urls = set(url_file.read().splitlines())

    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)
    else:
        # Exclude existing images
        urls = [url for url in urls if escape_image_name(url) not in os.listdir(output_directory)]

    # Build concurrent thread pool with max_image_fetching_threads
    with ThreadPoolExecutor(max_fetching_threads) as pool:
        futures = [
            pool.submit(
                download_image_with_timeout,
                url,
                download_timeout,
                output_directory,
            )
            for url in urls
        ]
        if verbose:
            for _ in tqdm(as_completed(futures)):
                pass
        else:
            wait(futures)

    return len(os.listdir(output_directory))
