def is_alphanumeric(string):
    return all(char.isalnum() or char.isspace() for char in string)

def validate_directory(directory):
    if not isinstance(directory, str):
        raise TypeError("directory must be a string, "+directory+" is not")
    if not is_alphanumeric(directory):
        raise ValueError("directory must be alphanumeric ('/' added automatically)")

def validate_extensions(extensions):
    if not isinstance(extensions, list):
        raise TypeError("extensions must be a list")
    for extension in extensions:
        if not extension.isalpha():
            raise ValueError("extensions must be alpha, "+extension+" is not")

def validate_headers(headers):
    if not isinstance(headers, dict):
        raise TypeError("headers must be a dict, "+headers+" is not")
    if 'User-Agent' not in headers:
        raise ValueError("headers must contain User-Agent")

def validate_total_images(total_images):
    if not isinstance(total_images, int):
        raise TypeError("total_images must be an integer, "+total_images+" is not")
    if total_images < 1:
        raise ValueError("total_images must be greater than 0")

def validate_search_term(search_term):
    if not isinstance(search_term, str):
        raise ValueError("search_term must be a string")
    if not is_alphanumeric(search_term):
        raise ValueError("search_term must be alphanumeric")

def validate_bool(var, name):
    if not isinstance(var, bool):
        raise TypeError(name+" must be a bool")

def validate_image_fetching_arguments(total_images, extensions, headers, directory, verbose, progress_bar):
    validate_total_images(total_images)
    validate_extensions(extensions)
    validate_headers(headers)
    validate_directory(directory)
    validate_bool(verbose,"verbose")
    validate_bool(progress_bar,"progress_bar")

def validate_download_images_params(search_term, total_images, extensions, headers, directory, verbose, progress_bar):
    validate_search_term(search_term)
    validate_image_fetching_arguments(total_images, extensions, headers, directory, verbose, progress_bar)

def validate_download_image_params(url, directory, headers, existing_images, extensions, raise_errors):
    if not isinstance(url, str):
        raise ValueError("url must be a string")
    validate_directory(directory)
    validate_headers(headers)
    if existing_images and not isinstance(existing_images, list):
        raise TypeError("existing_images must be a list")
    validate_extensions(extensions)
    validate_bool(raise_errors,"raise_errors")
    
def validate_concurrent_image_fetch_params(search_terms, total_images, headers, max_similtanous_threads, max_image_fetching_threads, extensions, directory, progress_bar, verbose):
    if search_terms and not isinstance(search_terms, list):
        raise TypeError("search_terms must be a list")
    for search_term in search_terms:
        validate_search_term(search_term)
    validate_image_fetching_arguments(total_images, extensions, headers, directory, verbose, progress_bar)
