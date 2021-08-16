import os
from shutil import rmtree

from image_fetcher.tools import escape_image_name
from image_fetcher.download_images import download_image, download_image_with_timeout, multi_thread_image_download


def reset_directory(directory):
    if os.path.isdir(directory):
        rmtree(directory)
    os.mkdir(directory)


IMAGE_DIRECTORY = "images"
URL_FILE = os.path.join("tests", "urls.txt")
with open(URL_FILE) as f:
    URLS = [line.strip() for line in f.readlines()]



class TestDownloadImages:
    def test_download_image(self):
        reset_directory(IMAGE_DIRECTORY)
        url = URLS[0]

        download_image(url, IMAGE_DIRECTORY)

        file_name = escape_image_name(url)
        assert file_name in os.listdir(IMAGE_DIRECTORY)
        assert os.path.getsize(os.path.join(IMAGE_DIRECTORY, file_name)) > 0

    def test_download_image_with_timeout_within_time(self):
        reset_directory(IMAGE_DIRECTORY)
        timeout = 5
        url = URLS[0]

        successful = download_image_with_timeout(url, timeout, IMAGE_DIRECTORY)

        assert successful
        file_name = escape_image_name(url)
        assert file_name in os.listdir(IMAGE_DIRECTORY)
        assert os.path.getsize(os.path.join(IMAGE_DIRECTORY, file_name)) > 0

    def test_download_image_with_timeout_exceed_time(self):
        reset_directory(IMAGE_DIRECTORY)
        timeout = 0
        url = URLS[0]

        successful = download_image_with_timeout(url, timeout, IMAGE_DIRECTORY)

        assert not successful
        file_name = escape_image_name(url)
        assert file_name not in os.listdir(IMAGE_DIRECTORY)

    def test_multi_thread_image_download(self):
        reset_directory(IMAGE_DIRECTORY)

        total_images = multi_thread_image_download(
            URL_FILE,
            IMAGE_DIRECTORY,
            max_fetching_threads=2,
            download_timeout=5,
            verbose=False,
        )
        assert total_images == len(URLS)
        for url in URLS:
            file_name = escape_image_name(url)
            assert file_name in os.listdir(IMAGE_DIRECTORY)
            assert os.path.getsize(os.path.join(IMAGE_DIRECTORY, file_name)) > 0

    def test_multi_thread_image_download_list(self):
        reset_directory(IMAGE_DIRECTORY)

        total_images = multi_thread_image_download(
            [
                "https://benaandrew.github.io/images/sentiment.jpg",
                "https://benaandrew.github.io/images/dog.jpg"
            ],
            IMAGE_DIRECTORY,
            max_fetching_threads=2,
            download_timeout=5,
            verbose=False,
        )
        assert total_images == len(URLS)
        for url in URLS:
            file_name = escape_image_name(url)
            assert file_name in os.listdir(IMAGE_DIRECTORY)
            assert os.path.getsize(os.path.join(IMAGE_DIRECTORY, file_name)) > 0

    @classmethod
    def teardown_class(cls):
        rmtree(IMAGE_DIRECTORY)
