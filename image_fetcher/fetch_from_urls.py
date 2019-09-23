from urllib import request
from re import sub
from json import loads

search = 'https://www.google.com/search?tbm=isch&q='

def download_url(url, headers):
    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    data = resp.read()
    resp.close()
    return data

def get_image_url(page):
    #Extract HTML about the image from source
    start_line = page.find('class="rg_meta notranslate">')
    start_object = page.find('{', start_line + 1)
    end_object = page.find('</div>', start_object + 1)
    object_raw = page[start_object:end_object]
    #Convert to values into a dictionary
    object_decode = bytes(object_raw, "utf-8").decode("unicode_escape")
    #Return the image source and where it searched up to
    final_image_url = loads(object_decode)["ou"]
    return final_image_url, end_object

def get_extension(url):
    return url.split(".")[-1]

def escape_image_name(url):
    #Remove extension
    escaped = url[:len(url)-len(url.split('.')[1])-1]
    #Remove http:// or https://
    escaped = escaped.split('/',1)[1]
    #Remove all non alphanumeric characters
    return sub("[^a-zA-Z0-9]+", '', escaped)

def download_page(search_term, headers):
    return str(download_url(search+search_term, headers))
