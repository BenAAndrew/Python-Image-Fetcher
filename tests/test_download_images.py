import os

from image_fetcher.tools import escape_image_name, convert_list_to_text_file
from image_fetcher.download_images import download_image, download_image_with_timeout, multi_thread_image_download
from image_fetcher.fetch_urls import fetch_images_from_yahoo
from tests.helpers import get_test_chromedriver_configuration, reset_directory, TestConfig


class TestDownloadImages:
    driver = get_test_chromedriver_configuration()
    urls = fetch_images_from_yahoo(driver, "cat", 5)

    def test_download_image(self):
        reset_directory(TestConfig.IMAGE_DIRECTORY)
        url = self.urls[0]

        download_image(url, TestConfig.IMAGE_DIRECTORY, TestConfig.HEADERS)

        file_name = escape_image_name(url)
        assert file_name in os.listdir(TestConfig.IMAGE_DIRECTORY)
        assert os.path.getsize(os.path.join(TestConfig.IMAGE_DIRECTORY, file_name)) > 0

    def test_download_image_with_timeout_within_time(self):
        reset_directory(TestConfig.IMAGE_DIRECTORY)
        timeout = 5
        url = self.urls[0]

        download_image_with_timeout(url, timeout, TestConfig.IMAGE_DIRECTORY, TestConfig.HEADERS)

        file_name = escape_image_name(url)
        assert file_name in os.listdir(TestConfig.IMAGE_DIRECTORY)

    def test_download_image_with_timeout_exceed_time(self):
        reset_directory(TestConfig.IMAGE_DIRECTORY)
        timeout = 0
        url = self.urls[0]

        download_image_with_timeout(url, timeout, TestConfig.IMAGE_DIRECTORY, TestConfig.HEADERS)

        file_name = escape_image_name(url)
        assert file_name not in os.listdir(TestConfig.IMAGE_DIRECTORY)

    def test_multi_thread_image_download_list(self):
        reset_directory(TestConfig.IMAGE_DIRECTORY)
        image_threads = 2
        timeout = 5

        total_images = multi_thread_image_download(
            self.urls, TestConfig.HEADERS, image_threads, timeout, TestConfig.IMAGE_DIRECTORY, verbose=False
        )
        assert total_images == len(self.urls)
        for url in self.urls:
            file_name = escape_image_name(url)
            assert file_name in os.listdir(TestConfig.IMAGE_DIRECTORY)

    def test_multi_thread_image_download_text_file(self):
        reset_directory(TestConfig.IMAGE_DIRECTORY)
        convert_list_to_text_file(self.urls, TestConfig.URL_LIST_FILE)
        image_threads = 2
        timeout = 5

        total_images = multi_thread_image_download(
            TestConfig.URL_LIST_FILE,
            TestConfig.HEADERS,
            image_threads,
            timeout,
            TestConfig.IMAGE_DIRECTORY,
            verbose=False,
        )
        assert total_images == len(self.urls)
        for url in self.urls:
            file_name = escape_image_name(url)
            assert file_name in os.listdir(TestConfig.IMAGE_DIRECTORY)
