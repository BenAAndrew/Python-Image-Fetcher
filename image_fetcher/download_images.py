import os
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

from func_timeout import func_timeout, FunctionTimedOut
from tqdm import tqdm

from image_fetcher.tools import escape_image_name, download_url


def download_image_simple_with_timeout(url: str, timeout: int, directory: str, headers):
    """
    Downloads image from given URL. Will exit if not complete within timeout seconds. Doesn't validate input params.

    Parameters:
    url (str): URL to try and download image from
    timeout (int): seconds to wait for function to execute
    directory (str): directory to save image to
    headers (dict): headers for the urllib file request
    """
    try:
        func_timeout(timeout, download_image, args=(url, directory, headers,))
    except FunctionTimedOut:
        pass


def download_image(url: str, directory: str, headers: dict):
    """
    Downloads image from given URL.

    Parameters:
    url (str): URL to try and download image from
    directory (str): directory to save image to
    headers (dict): headers for the urllib file request
    """
    image_name = escape_image_name(url)
    data = download_url(url, headers)
    with open(directory + "/" + image_name, "wb") as output_file:
        output_file.write(data)


def multi_thread_image_download(
    urls,
    headers: dict,
    max_image_fetching_threads: int,
    image_download_timeout: int,
    directory: str,
    verbose=True,
):
    if not os.path.isdir(directory):
        os.mkdir(directory)
    else:
        # Exclude existing images
        urls = [url for url in urls if escape_image_name(url) not in os.listdir(directory)]

    # Build concurrent thread pool with max_image_fetching_threads
    with ThreadPoolExecutor(max_image_fetching_threads) as pool:
        futures = [
            pool.submit(
                download_image_simple_with_timeout,
                url,
                image_download_timeout,
                directory,
                headers,
            )
            for url in urls
        ]
        if verbose:
            for f in tqdm(as_completed(futures)):
                pass
        else:
            wait(futures)

    return len(os.listdir(directory))
