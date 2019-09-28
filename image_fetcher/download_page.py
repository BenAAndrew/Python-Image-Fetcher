from image_fetcher.tools import round_up_to_nearest_hundred

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


wait_time = 1
#As some URL's will likely fail, It's a good idea to fetch more than we need
#The backup_threshold is what amount to multiple needed URL's by
#At a rating of 2, for 200 images we'd fetch 400 URL's (leaving 200 to spare)
backup_threshold = 2
google_images = 'https://www.google.com/search?tbm=isch&q='

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')

def download_page(search_term, total_images):
    browser = webdriver.Chrome('chromedriver.exe', options=options)
    browser.get(google_images+search_term)
    total_images *= backup_threshold
    required_scrolls = int(round_up_to_nearest_hundred(total_images) / 100)-1
    for i in range(0, required_scrolls):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(wait_time)
    source = browser.page_source
    browser.close()
    return BeautifulSoup(source, 'html.parser')
