def validate_directory(directory):
    if not isinstance(directory, str):
        raise TypeError("directory must be a string")
    if not directory.isalnum():
        raise ValueError("directory must be alphanumeric ('/' added automatically)")

def validate_extensions(extensions):
    if not isinstance(extensions, list):
        raise TypeError("extensions must be a list")
    for extension in extensions:
        if not extension.isalpha():
            raise ValueError("extensions must be alpha, "+extension+" is not")

def validate_headers(headers):
    if not isinstance(headers, dict):
        raise TypeError("headers must be a dict")
    if 'User-Agent' not in headers:
        raise ValueError("headers must contain User-Agent")

def validate_download_images_params(search_term, total_images, extensions, headers, directory, verbose, progress_bar):
    if not isinstance(search_term, str):
        raise ValueError("search_term must be a string")
    if not search_term.isalnum():
        raise ValueError("search_term must be alphanumeric")
    if not isinstance(total_images, int):
        raise TypeError("total_images must be an integer")
    if total_images < 1:
        raise ValueError("total_images must be greater than 0")
    validate_extensions(extensions)
    validate_headers(headers)
    validate_directory(directory)
    if not isinstance(verbose, bool):
        raise TypeError("verbose must be a bool")
    if not isinstance(progress_bar, bool):
        raise TypeError("progress_bar must be a bool")

def validate_download_image_params(url, directory, headers, existing_images, extensions, raise_errors):
    if not isinstance(url, str):
        raise ValueError("url must be a string")
    validate_directory(directory)
    validate_headers(headers)
    if existing_images and not isinstance(existing_images, list):
        raise TypeError("existing_images must be a list")
    validate_extensions(extensions)
    if not isinstance(raise_errors, bool):
        raise TypeError("raise_errors must be a bool")
    