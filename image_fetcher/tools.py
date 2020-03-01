from re import sub
from urllib import request


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


def get_extension(url):
    return url.split(".")[-1]


def escape_image_name(url):
    """
    Get URL without extension and 'http(s)://' and removes all non alphanumeric characters

    Parameters:
    url (str): URL to escape

    Returns:
    str: Escaped URL
    """
    #Remove extension
    escaped = url[:len(url)-len(url.split('.')[1])-1]
    #Remove http:// or https://
    escaped = escaped.split('/',1)[1]
    #Remove all non alphanumeric characters
    return sub("[^a-zA-Z0-9]+", '', escaped)
