from re import sub
from urllib import request


def download_url(url: str, headers: dict):
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


def escape_image_name(url: str):
    """
    Remove 'http(s)://' and all non alphanumeric characters from file URL

    Parameters:
    url (str): URL to escape

    Returns:
    str: Escaped URL
    """
    extension = url.split(".")[-1]
    # Remove extension
    escaped = url[: -len(extension) - 1]
    # Remove http:// or https://
    escaped = escaped.split("/", 1)[1]
    # Remove all non alphanumeric characters
    return f"{sub('[^a-zA-Z0-9]+', '', escaped)}.{extension}"
