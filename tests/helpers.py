import os
from shutil import rmtree


class TestConfig:
    IMAGE_DIRECTORY = "images"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    }
    URL_FILE = os.path.join("tests", "urls.txt")
    with open(URL_FILE) as f:
        URLS = [line.strip() for line in f.readlines()]


def reset_directory(directory):
    if os.path.isdir(directory):
        rmtree(directory)
    os.mkdir(directory)
