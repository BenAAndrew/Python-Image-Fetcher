from download_images import download_images
from concurrent.futures import ThreadPoolExecutor


def multithread_image_fetching(search_terms, total_images, headers, extensions=['jpg','png'], directory=None, progress_bar=True, verbose=True):
    array = [(search_term, total_images, headers, extensions, directory, progress_bar, verbose) for search_term in search_terms]
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(download_images, *zip(*array))

multithread_image_fetching(
    search_terms=['cat','dog'], 
    total_images=10, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
)
