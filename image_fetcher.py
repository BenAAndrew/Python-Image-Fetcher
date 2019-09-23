from fetch_from_urls import download_url, download_page, get_extension, escape_image_name, get_image_url
from validate_params import validate_download_images_params, validate_download_image_params, validate_directory
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
    page = download_page(search_term, headers)
    #Check if any images already exist to avoid wasting time re-downloading them
    existing_images = get_existing_images(directory+'/')
    total_already_existing = 0
    total_downloaded = 0
    #If progress bar initialise tqdm
    if progress_bar:
        pbar = tqdm(total=total_images)
    
    #Download images up to given amount
    while total_downloaded+total_already_existing < total_images:
        final_image_url, end_object = get_image_url(page)
        #Remove already processed section of HTML from the page
        page = page[end_object:]
        image = download_image(final_image_url, directory, headers, existing_images, extensions)
        if image:
            #if image was downloaded
            if image == 1:
                total_downloaded+=1
            #if image was ignored as it was already found
            else:
                total_already_existing+=1
            if progress_bar:
                pbar.update(1)
    
    if progress_bar:
        pbar.close()
    if verbose:
        print("Total downloaded = "+str(total_downloaded))
        print("Total ignored as they already existed = "+str(total_already_existing))


download_images(
        search_term='abc', 
        total_images=10, 
        extensions=['jpg', 'png'], 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    )