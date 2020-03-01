from image_fetcher.fetch_urls import fetch_images_from_yahoo
from tests.helpers import get_test_chromedriver_configuration


class TestFetchUrls:
    def test_fetch_images_from_yahoo(self):
        driver = get_test_chromedriver_configuration()
        file_types = ["jpg"]
        search_term = "cat"
        total_images = 5
        image_urls = fetch_images_from_yahoo(driver, search_term, total_images, file_types=file_types)
        assert len(image_urls) == 5
        for url in image_urls:
            assert url.split(".")[-1] in file_types
