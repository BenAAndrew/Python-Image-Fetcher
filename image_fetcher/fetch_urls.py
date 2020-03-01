from time import sleep


def fetch_images_from_yahoo(driver, total_images):
    driver.get("https://images.search.yahoo.com/search/images;_ylt=AwrJ6wpW01pe8XIAgY2LuLkF;_ylc=X1MDOTYwNTc0ODMEX3IDMgRmcgMEZ3ByaWQDbzhOdGw3UkpURzZlR0ZDbTdhcHFDQQRuX3N1Z2cDNQRvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDMwRxdWVyeQNhYmMEdF9zdG1wAzE1ODMwMTEwMDk-?p=123")
    driver.find_element_by_css_selector("button[type=\"submit\"]").click()

    icons = driver.find_element_by_tag_name("img").click()
    urls = set()
    while len(urls) < total_images:
        image_src = driver.find_element_by_id("img").get_attribute("src")
        if image_src.endswith(".jpg") or image_src.endswith(".png"):
            urls.add(image_src)
        sleep(0.5)
        driver.find_element_by_css_selector(".nav.right").click()

    driver.close()
    return urls
