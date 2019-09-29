from selenium import webdriver
from enum import Enum
from os.path import abspath
from os import listdir


class BrowserType(Enum):
    CHROME = 1
    FIREFOX = 2


def validate_driver(driver_path):
    if "/" in driver_path:
        driver = driver_path.split("/")[-1]
        directory = driver_path[0:len(driver_path)-len(driver)-1]
        if not driver in listdir(directory):
            raise ValueError(driver+" not found in "+directory)
    else:
        driver = driver_path
        if not driver in listdir():
            raise ValueError(driver+" not found in current directory")


class Browser:
    def __init__(self, browser_type, driver):
        validate_driver(driver)
        self.browser_type = browser_type
        if browser_type == BrowserType.CHROME:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')
            self.driver = driver
            self.options = chrome_options
        elif browser_type == BrowserType.FIREFOX:
            firefox_options = webdriver.firefox.options.Options()
            firefox_options.headless = True
            self.driver = abspath(driver)
            self.options = firefox_options
        else:
            raise ValueError("driver_type not valid, choose from: "+str(list(Browser)))
