from image_fetcher.get_image_urls import get_image_urls
from image_fetcher.validate_params import validate_download_images_params
from image_fetcher.download_page import download_page
from image_fetcher.download_image import download_image
from image_fetcher.tools import get_existing_images, print_summary
from image_fetcher.browsers import Browser, BrowserType

from tqdm import tqdm


def download_images(search_term, total_images, headers, browser, 
extensions=['jpg','png'], directory=None, progress_bar=True, verbose=True):
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
    validate_download_images_params(search_term, total_images, extensions, headers, browser, directory, verbose, progress_bar)
    #Setup variables
    #Download raw HTML from google image search of given term
    page = download_page(search_term, total_images, browser)
    #Get list of iamge URLS from the page
    urls = get_image_urls(page, verbose=verbose)

    existing_images = get_existing_images(directory)
    images_in_folder = len(existing_images)
    total_downloaded = 0
    #If progress bar initialise tqdm
    if progress_bar:
        pbar = tqdm(total=total_images)
        pbar.update(images_in_folder)
    
    #Download urls from url list
    url_index = 0
    while total_downloaded+images_in_folder < total_images:
        #Try to download next URL
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
            page = download_page(search_term, total_images+100, browser)
            urls = get_image_urls(page, verbose=verbose)

    if progress_bar:
        pbar.close()
    if verbose:
        print_summary(search_term, total_downloaded=total_downloaded, total_ignored=images_in_folder)
