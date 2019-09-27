from urllib import request
from re import sub
from json import loads


def download_url(url, headers):
    """
    Read data from a given URL

    Parameters:
    url (str): URL to retrieve data from
    headers (dict): Headers for urllib to use when requesting from urls (must include 'User-Agent')

    Returns:
    bytes: Returns bytes of data from the URL
    """
    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    data = resp.read()
    resp.close()
    return data

def get_image_urls(page, verbose=True):
    """
    Get a list of URL's from a given google search page

    Parameters:
    page (str): HTML source of a google image search
    verbose (bool): Whether to print total URL's found (defaults to True)

    Returns:
    list: Returns list of image URL's
    """
    image_urls = []
    #Get all image source URLS
    for image_html in page.find_all("div",{"class":"rg_meta"}):
        try:
            #Add the image source to urls
            final_image_url = loads(image_html.text)["ou"]
            image_urls.append(final_image_url)
        except:
            break
    if verbose:
        print(str(len(image_urls))+" image urls found")
    return image_urls

def get_extension(url):
    return url.split(".")[-1]

def escape_image_name(url):
    #Remove extension
    escaped = url[:len(url)-len(url.split('.')[1])-1]
    #Remove http:// or https://
    escaped = escaped.split('/',1)[1]
    #Remove all non alphanumeric characters
    return sub("[^a-zA-Z0-9]+", '', escaped)
