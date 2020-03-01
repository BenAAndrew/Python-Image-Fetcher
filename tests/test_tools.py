from image_fetcher.tools import escape_image_name, convert_list_to_text_file
from tests.helpers import TestConfig


class TestTools:
    def test_escape_image_name_http(self):
        url = "http://www.fakewebsite.com/sample.jpg"
        result = escape_image_name(url)
        assert result == "wwwfakewebsitecomsample.jpg"

    def test_escape_image_name_https(self):
        url = "https://www.fakewebsite.com/sample.jpg"
        result = escape_image_name(url)
        assert result == "wwwfakewebsitecomsample.jpg"

    def test_escape_image_name_non_alphanumeric_characters(self):
        url = "https://www.fakewebsite!.com/sample$_.jpg"
        result = escape_image_name(url)
        assert result == "wwwfakewebsitecomsample.jpg"

    def test_convert_list_to_text_file(self):
        urls = ["dog.jpg", "cat.png", "duck.gif"]
        convert_list_to_text_file(urls, TestConfig.URL_LIST_FILE)

        with open(TestConfig.URL_LIST_FILE, "r") as url_list_file:
            urls_in_file = url_list_file.read().splitlines()

        for url in urls:
            assert url in urls_in_file
