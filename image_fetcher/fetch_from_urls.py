from urllib import request
from re import sub
from json import loads


def download_url(url, headers):
    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    data = resp.read()
    resp.close()
    return data

def get_image_urls(page, total_images, text_file=True, verbose=True):
    image_urls = []
    for image_html in page.find_all("div",{"class":"rg_meta"}):
        try:
            #Return the image source and where it searched up to
            final_image_url = loads(image_html.text)["ou"]
            image_urls.append(final_image_url)
        except:
            break
    if verbose:
        print(str(len(image_urls))+" image urls found")
    return image_urls[:total_images+1]

def get_extension(url):
    return url.split(".")[-1]

def escape_image_name(url):
    #Remove extension
    escaped = url[:len(url)-len(url.split('.')[1])-1]
    #Remove http:// or https://
    escaped = escaped.split('/',1)[1]
    #Remove all non alphanumeric characters
    return sub("[^a-zA-Z0-9]+", '', escaped)
