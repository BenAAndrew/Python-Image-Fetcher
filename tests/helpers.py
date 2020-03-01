import os

from selenium import webdriver


class TestConfig:
    IMAGE_DIRECTORY = "test"
    URL_LIST_FILE = "test_url_list.txt"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    }


def reset_directory(directory):
    if os.path.isdir(directory):
        for f in os.listdir(directory):
            os.remove(os.path.join(directory, f))
    else:
        os.mkdir(directory)


def get_test_chromedriver_configuration():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    return webdriver.Chrome("../chromedriver.exe", options=options)
