from re import sub
from urllib import request


def download_url(url: str):
    """
    Read data from a given URL

    Parameters:
    url (str): URL to retrieve data from

    Returns:
    bytes: Returns bytes of data from the URL
    """
    req = request.Request(url)
    with request.urlopen(req) as resp:
        data = resp.read()
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
