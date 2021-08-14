from image_fetcher.tools import escape_image_name


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
