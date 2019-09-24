from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from math import ceil

wait_time = 1
google_images = 'https://www.google.com/search?tbm=isch&q='

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
browser = webdriver.Chrome('chromedriver.exe', options=options)

def round_up_to_nearest_hundred(x):
    return int(ceil(x / 100.0)) * 100

def download_page(search_term, total_images):
    browser.get(google_images+search_term)
    required_scrolls = int(round_up_to_nearest_hundred(total_images) / 100)-1
    for i in range(0, required_scrolls):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(wait_time)
    source = browser.page_source
    browser.close()
    return BeautifulSoup(source, 'html.parser')
