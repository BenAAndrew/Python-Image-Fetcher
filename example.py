from image_fetcher.download_images import multithread_image_download
from image_fetcher.fetch_urls import fetch_images_from_yahoo
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
driver = webdriver.Chrome("chromedriver.exe", options=options)

search_term = "cat"
total_images = 10

urls = fetch_images_from_yahoo(driver, search_term, total_images)

multithread_image_download(
    urls,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'},
    max_image_fetching_threads=1,
    image_download_timeout=5,
    directory=search_term
)
