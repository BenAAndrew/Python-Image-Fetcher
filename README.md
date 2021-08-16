# Python Image Fetcher
A simple lightweight library to download images (and other files)

## Install
With [Python 3.5+](https://www.python.org/) run:
```
pip install image-fetcher
```


## Key features
* **Speed:** By using multi-threading, more images can be downloaded per second
* **No download duplication:** To avoid unnecessary downloads
* **Progress bar:** To track how your download is getting on


## Usage
The simplest usage involves passing a list of URL's and the folder you want the images to be saved to:
```
from image_fetcher import multi_thread_image_download

multi_thread_image_download(
    ["https://benaandrew.github.io/images/sentiment.jpg","https://benaandrew.github.io/images/dog.jpg"],
    "images",
)
```

If you have your URL's saved in my text file you can also give the path to that file
```
multi_thread_image_download(
    "urls.txt",
    "images",
)
```

## Additional arguments
- **max_fetching_threads** (int): Sets the maximum number of concurrent image downloads 
    - Increasing this increases download throughput but also uses more processing power and can cause errors when set too high
    - By default is set the number of cpu cores x 5
- **download_timeout** (int): Seconds before a download is abandoned
    - Increasing this means more time will be allowed per download. If every download is important you should set this high
    - The default is 5 seconds
- **verbose** (bool): Whether to show progress bar
    - On by default

You can pass these like so:
```
multi_thread_image_download(
    "urls.txt",
    "images",
    max_fetching_threads=5,
    download_timeout=10,
    verbose=False
)
```
