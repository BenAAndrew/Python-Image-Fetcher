from image_fetcher.get_image_urls import download_url
from image_fetcher.tools import get_extension, escape_image_name
from image_fetcher.validate_params import validate_download_image_params
from image_fetcher.download_page import download_page

from tqdm import tqdm
from os import listdir
from func_timeout import func_timeout, FunctionTimedOut


def download_image_simple_with_timeout(url, timeout, directory, headers, existing_images=[], extensions=['jpg','png']):
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
        func_timeout(timeout, download_image_simple, args=(url, directory, headers, existing_images, extensions,))
    except FunctionTimedOut:
        pass


def download_image_simple(url, directory, headers, existing_images=[], extensions=['jpg','png']):
    """
    Downloads image from given URL. Doesn't validate input params.

    Parameters:
    url (str): URL to try and download image from
    directory (str): directory to save image to
    existing_images (list): list of existing images to avoid trying to download an existing image 
    (can be fetched by passing the folder name to get_existing_images(), default is []) 
    extensions (list): Image file extensions to accept (defaults to 'jpg' and 'png')
    """
    try:
        if get_extension(url) in extensions:
            image_name = escape_image_name(url)+'.'+get_extension(url)
            if image_name not in existing_images:
                data = download_url(url, headers)
                output_file = open(directory+'/'+image_name, 'wb')
                output_file.write(data)
                output_file.close()
    except:
        pass


def download_image(url, directory, headers, existing_images=[], extensions=['jpg','png'], raise_errors=False):
    """
    Downloads image from given URL and returns status code

    Parameters:
    url (str): URL to try and download image from
    directory (str): directory to save image to
    existing_images (list): list of existing images to avoid trying to download an existing image 
    (can be fetched by passing the folder name to get_existing_images(), default is []) 
    extensions (list): Image file extensions to accept (defaults to 'jpg' and 'png')
    raise_errors (bool): Whether to raise an error if one occurs during download (default is False)

    Returns:
    int: Returns 1 if an image was downloaded, 2 if the download was ignored as the image already existed, 
    or 0 if it failed/was aborted due to invalid file type
    """
    validate_download_image_params(url, directory, headers, existing_images, extensions, raise_errors)
    try:
        if get_extension(url) in extensions:
            #Convert escaped URL to the image name (used to ensure same image isn't downloaded again in future)
            image_name = escape_image_name(url)+'.'+get_extension(url)
            if image_name not in existing_images:
                data = download_url(url, headers)
                #Write data from URL request to image
                output_file = open(directory+'/'+image_name, 'wb')
                output_file.write(data)
                output_file.close()
                if image_name in listdir(directory):
                    return 1
            else:
                return 2
    except:
        if raise_errors:
            raise 
        pass
    return 0
