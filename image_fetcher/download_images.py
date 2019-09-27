from get_image_urls import download_url, get_extension, escape_image_name, get_image_urls
from validate_params import validate_download_images_params, validate_download_image_params, validate_directory
from download_page import download_page
from tqdm import tqdm
from os import listdir, mkdir


def get_existing_images(directory):
    """
    Get's a list of files in a given directory or creates it if the directory doesn't exist

    Parameters:
    directory (str): directory to search

    Returns:
    list: Returns list of files in the directory (expty if the directory didn't exist)
    """
    validate_directory(directory)
    directory += '/'
    try:
        return listdir(directory)
    except:
        mkdir(directory)
        return []


def download_image(url, directory, headers, existing_images=None, extensions=['jpg','png'], raise_errors=False):
    """
    Downloads image from given URL

    Parameters:
    url (str): URL to try and download image from
    directory (str): directory to save image to
    existing_images (list): list of existing images to avoid trying to download an existing image 
    (can be fetched by passing the folder name to get_existing_images(), default is None) 
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
            if not existing_images or image_name not in existing_images:
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


def download_images(search_term, total_images, headers, extensions=['jpg','png'], directory=None, progress_bar=True, verbose=True):
    """
    Downloads images from google for given search_term

    Parameters:
    search_term (str): Given term for downloading images from google
    total_images (int): Total number of images to download (will skip identical images in the given directory)
    headers (dict): Headers for urllib to use when requesting from urls (must include 'User-Agent')
    extensions (list): Image file extensions to accept (defaults to 'jpg' and 'png')
    directory (str): Directory to save images to (defaults to naming folder same as search_term)
    progress_bar (bool): Whether to display progress bar during downloading (defaults to True)
    verbose (bool): Whether to print total downloaded & total ignored at the end (defaults to True)
    """
    if not directory:
        directory = search_term
    #Validate passed params
    validate_download_images_params(search_term, total_images, extensions, headers, directory, verbose, progress_bar)
    #Setup variables
    #Download raw HTML from google image search of given term
    page = download_page(search_term, total_images)
    #Get list of iamge URLS from the page
    urls = get_image_urls(page, verbose=verbose)

    existing_images = get_existing_images(directory)
    total_already_existing = len(existing_images)
    total_downloaded = 0
    #If progress bar initialise tqdm
    if progress_bar:
        pbar = tqdm(total=total_images)
    pbar.update(total_already_existing)
    
    #Download urls from url list
    url_index = 0
    while total_downloaded+total_already_existing < total_images:
        #Remove already processed section of HTML from the page
        image = download_image(urls[url_index], directory, headers, existing_images, extensions)
        url_index += 1
        if image:
            #if image was downloaded
            if image == 1:
                total_downloaded+=1
            if progress_bar:
                pbar.update(1)
        #If we've run out of URL's due to them being erroneous we'll get more
        if url_index == len(urls):
            if verbose:
                print("All URL's attempted, fetching more")
            page = download_page(search_term, total_images+100)
            urls = get_image_urls(page, verbose=verbose)

    if progress_bar:
        pbar.close()
    if verbose:
        print("Total downloaded = "+str(total_downloaded))
        print("Total ignored as they already existed = "+str(total_already_existing))
