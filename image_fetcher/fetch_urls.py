from time import sleep


def fetch_images_from_yahoo(driver, search_term, total_images, file_types=["jpg", "png"]):
    """
    Example image fetching process using yahoo image search
    """
    driver.get(
        "https://images.search.yahoo.com/search/images;_ylt=AwrJ6wpW01pe8XIAgY2LuLkF;_ylc=X1MDOTYwNTc0ODMEX3IDMgRmcgMEZ3ByaWQDbzhOdGw3UkpURzZlR0ZDbTdhcHFDQQRuX3N1Z2cDNQRvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDMwRxdWVyeQNhYmMEdF9zdG1wAzE1ODMwMTEwMDk-?p="
        + search_term
    )
    driver.find_element_by_css_selector('button[type="submit"]').click()

    icons = driver.find_element_by_tag_name("img").click()
    urls = set()
    while len(urls) < total_images:
        image_src = driver.find_element_by_id("img").get_attribute("src")
        if image_src.split(".")[-1] in file_types:
            urls.add(image_src)
        sleep(0.5)
        driver.find_element_by_css_selector(".nav.right").click()

    return list(urls)
