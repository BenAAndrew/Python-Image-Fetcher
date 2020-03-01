import os
from concurrent.futures import ThreadPoolExecutor, wait
from os import mkdir, listdir

from func_timeout import func_timeout, FunctionTimedOut
from image_fetcher.tools import escape_image_name, get_extension, download_url


def download_image_simple_with_timeout(url, timeout, directory, headers):
    """
    Downloads image from given URL. Will exit if not complete within timeout seconds. Doesn't validate input params.

    Parameters:
    url (str): URL to try and download image from
    timeout (int): Seconds to wait for function to execute
    directory (str): directory to save image to
    existing_images (list): list of existing images to avoid trying to download an existing image
    (can be fetched by passing the folder name to get_existing_images(), default is [])
    extensions (list): Image file extensions to accept (defaults to 'jpg' and 'png')
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
    try:
        image_name = escape_image_name(url)+'.'+get_extension(url)
        data = download_url(url, headers)
        output_file = open(directory+'/'+image_name, 'wb')
        output_file.write(data)
        output_file.close()
    except:
        pass


def multithread_image_download(urls, headers: dict, max_image_fetching_threads: int, image_download_timeout: int, directory: str, verbose=True):
    total_images = len(urls)
    pool = ThreadPoolExecutor(max_image_fetching_threads)
    futures = []

    # TODO: Exclude existing images
    if not os.path.isdir(directory):
        mkdir(directory)

    # TODO: Remove existing images arg & extensions

    url_index = 0
    # Append maximum required number of threads (pool will limit the number of ones running concurrently)
    for url in urls:
        futures.append(
            pool.submit(download_image_simple_with_timeout, url, image_download_timeout, directory, headers))
        # Increment url_index so each call to download_image will take a different url
        url_index += 1

    # Wait for all threads to execute
    wait(futures)
    return len(listdir(directory))
