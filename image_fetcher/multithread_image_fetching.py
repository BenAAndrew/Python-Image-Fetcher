from image_fetcher.get_image_urls import get_image_urls
from image_fetcher.validate_params import validate_concurrent_images_download, validate_concurrent_image_search_params
from image_fetcher.download_images import get_existing_images
from image_fetcher.download_image import download_image_simple_with_timeout
from image_fetcher.download_page import download_page
from image_fetcher.tools import print_summary

from tqdm import tqdm
from os import listdir
from concurrent.futures import ThreadPoolExecutor, wait


def concurrent_images_download(search_term, total_images, headers, max_image_fetching_threads, image_download_timeout, 
browser, extensions=['jpg','png'], directory=None, progress_bar=True, verbose=True):
    """
    Downloads images from google for given search_term using multiple concurrent threads

    Parameters:
    search_term (str): Given term for downloading images from google
    total_images (int): Total number of images to download (will skip identical images in the given directory)
    headers (dict): Headers for urllib to use when requesting from urls (must include 'User-Agent')
    max_image_fetching_threads (int): Maximum number of similtaneously running image fetching threads
    extensions (list): Image file extensions to accept (defaults to 'jpg' and 'png')
    directory (str): Directory to save images to (defaults to naming folder same as search_term)
    progress_bar (bool): Whether to display progress bar during downloading (defaults to True)
    verbose (bool): Whether to print total downloaded & total ignored at the end (defaults to True)
    """
    if not directory:
        directory = search_term
    #Validate passed params
    validate_concurrent_images_download(search_term, total_images, headers, browser, max_image_fetching_threads, extensions, directory, progress_bar, verbose)
    #Setup variables
    #Download raw HTML from google image search of given term
    page = download_page(search_term, total_images, browser)
    #Get list of iamge URLS from the page
    urls = get_image_urls(page, verbose=verbose)

    #Setup thread executor pool and active threads list
    pool = ThreadPoolExecutor(max_image_fetching_threads)
    futures = []

    #Get existing images 
    existing_images = get_existing_images(directory)
    images_in_folder = len(existing_images)
    
    #If progress bar initialise tqdm
    if progress_bar:
        pbar = tqdm(total=total_images)
        pbar.update(images_in_folder)
    
    url_index = 0 
    while images_in_folder != total_images:
        #Append maximum required number of threads (pool will limit the number of ones running concurrently)
        for x in range(0, total_images-images_in_folder):
            futures.append(pool.submit(download_image_simple_with_timeout, urls[url_index], image_download_timeout, directory, headers, existing_images, extensions))
            #Increment url_index so each call to download_image will take a different url
            url_index+=1

        #Wait for all threads to execute
        wait(futures)

        if progress_bar:
            images_in_folder_before = images_in_folder
        #Count new total of images in the folder to either exit the loop or execute more threads
        images_in_folder = len(listdir(directory))
        if progress_bar:
            pbar.update(images_in_folder-images_in_folder_before)

        #If we've run out of URL's due to them being erroneous we'll get more
        if url_index+(total_images-images_in_folder) >= len(urls):
            if verbose:
                print("All URL's attempted, fetching more")
            page = download_page(search_term, total_images+100, browser.webdriver)
            urls = get_image_urls(page, verbose=verbose)

    if progress_bar:
        pbar.close()
    if verbose:
        print_summary(search_term, total_downloaded=total_images-len(existing_images), total_ignored=len(existing_images))


def concurrent_image_search(search_terms, total_images, headers, max_similtanous_threads, max_image_fetching_threads, 
image_download_timeout, browser, extensions=['jpg','png'], directories=None, progress_bar=True, verbose=True):
    """
    Downloads images from google for multiple search_terms using multiple concurrent threads

    Parameters:
    search_terms (list): List of search terms for downloading images from google
    total_images (int): Total number of images to download (will skip identical images in the given directory)
    headers (dict): Headers for urllib to use when requesting from urls (must include 'User-Agent')
    max_similtanous_threads (int): Maximum number of similtaneously running image search threads
    max_image_fetching_threads (int): Maximum number of similtaneously running image fetching downloading per image search
    extensions (list): Image file extensions to accept (defaults to 'jpg' and 'png')
    directories (list): Directories to save images to (defaults to naming folder same as search_term)
    progress_bar (bool): Whether to display progress bar during downloading (defaults to True)
    verbose (bool): Whether to print total downloaded & total ignored at the end (defaults to True)
    """
    if not directories:
        directories = search_terms
    #Validate passed params
    validate_concurrent_image_search_params(search_terms, total_images, headers, browser, max_similtanous_threads, max_image_fetching_threads, extensions, directories, progress_bar, verbose)
    #Setup thread executor pool and active threads list
    pool = ThreadPoolExecutor(max_image_fetching_threads)
    futures = []
    for i in range(0, len(search_terms)):
        #Add new concurrent_images_download process thread for each search term
        futures.append(pool.submit(concurrent_images_download, search_terms[i], total_images, headers, max_image_fetching_threads, image_download_timeout, browser, extensions, directories[i], progress_bar, verbose))
    #Wait for all threads to execute
    wait(futures)
