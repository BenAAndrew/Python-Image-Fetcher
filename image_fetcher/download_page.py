from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from math import ceil

wait_time = 1
#As some URL's will likely fail, It's a good idea to fetch more than we need
#The backup_threshold is what percentage extra to fetch (i.e. if 200 images were
# needed it would fetch 220 URL's)
backup_threshold = 0.1
google_images = 'https://www.google.com/search?tbm=isch&q='

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')


def round_up_to_nearest_hundred(x):
    return int(ceil(x / 100.0)) * 100

def download_page(search_term, total_images):
    browser = webdriver.Chrome('chromedriver.exe', options=options)
    browser.get(google_images+search_term)
    total_images *= 1 + backup_threshold
    required_scrolls = int(round_up_to_nearest_hundred(total_images) / 100)-1
    for i in range(0, required_scrolls):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(wait_time)
    source = browser.page_source
    browser.close()
    return BeautifulSoup(source, 'html.parser')
