from get_image_urls import get_image_urls
from validate_params import validate_download_images_params
from download_images import get_existing_images, download_image
from download_page import download_page
from tqdm import tqdm
from os import listdir, mkdir
from concurrent.futures import ThreadPoolExecutor, wait


def concurrent_images_download(search_term, total_images, headers, max_image_fetching_threads, extensions=['jpg','png'], directory=None, progress_bar=True, verbose=True):
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
    pool = ThreadPoolExecutor(max_image_fetching_threads)
    futures = []
    url_index = 0 
    
    images_in_folder = len(existing_images)
    while images_in_folder != total_images:
        for x in range(0, total_images-images_in_folder):
            futures.append(pool.submit(download_image, urls[url_index], directory, headers, existing_images, extensions))
            url_index+=1

        wait(futures)
        images_in_folder = len(listdir(directory))
    
    if verbose:
        print("Total downloaded = "+str(total_images-len(existing_images)))
        print("Total ignored as they already existed = "+str(len(existing_images)))


def concurrent_image_search(search_terms, total_images, headers, max_similtanous_threads, max_image_fetching_threads, extensions=['jpg','png'], directory=None, progress_bar=True, verbose=True):
    array = [(search_term, total_images, headers, max_image_fetching_threads, extensions, directory, progress_bar, verbose) for search_term in search_terms]
    with ThreadPoolExecutor(max_workers=max_similtanous_threads) as executor:
        executor.map(concurrent_images_download, *zip(*array))

concurrent_image_search(
    search_terms=['cat','dog'], 
    max_similtanous_threads=2,
    max_image_fetching_threads=10,
    total_images=10, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
)
