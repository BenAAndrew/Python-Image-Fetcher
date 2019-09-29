from image_fetcher.validate_params import validate_driver

from selenium import webdriver
from enum import Enum
from os.path import abspath


class BrowserType(Enum):
    CHROME = 1
    FIREFOX = 2


class Browser:
    def __init__(self, browser_type, driver):
        validate_driver(driver)
        if browser_type == BrowserType.CHROME:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')
            self.webdriver = webdriver.Chrome(driver, options=chrome_options)
        elif browser_type == BrowserType.FIREFOX:
            firefox_options = webdriver.firefox.options.Options()
            firefox_options.headless = True
            self.webdriver = webdriver.Firefox(executable_path=abspath(driver), options=firefox_options)
        else:
            raise ValueError("driver_type not valid, choose from: "+str(list(Browser)))
