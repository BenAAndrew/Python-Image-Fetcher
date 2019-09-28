from validate_params import validate_directory
from os import listdir, mkdir
from math import ceil
from re import sub


def get_existing_images(directory):
    """
    Get's a list of files in a given directory or creates it if the directory doesn't exist

    Parameters:
    directory (str): directory to search

    Returns:
    list: Returns list of files in the directory (expty if the directory didn't exist)
    """
    validate_directory(directory)
    directory += '/'
    try:
        return listdir(directory)
    except:
        mkdir(directory)
        return []


def get_extension(url):
    return url.split(".")[-1]


def escape_image_name(url):
    #Remove extension
    escaped = url[:len(url)-len(url.split('.')[1])-1]
    #Remove http:// or https://
    escaped = escaped.split('/',1)[1]
    #Remove all non alphanumeric characters
    return sub("[^a-zA-Z0-9]+", '', escaped)


def round_up_to_nearest_hundred(x):
    return int(ceil(x / 100.0)) * 100
