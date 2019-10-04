# Multi-Thread Multi-Search
Use this method when fetching from multiple image searches similtaneously

## Quick Start
```
from image_fetcher.multithread_image_fetching import concurrent_image_search
from image_fetcher.browsers import Browser, BrowserType

concurrent_image_search(
    search_terms=['cat','dog'], 
    max_similtanous_threads=2,
    max_image_fetching_threads=20,
    image_download_timeout=5,
    total_images=200, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'},
    browser=Browser(BrowserType.CHROME, 'chromedriver')
)
```

## Key arguments
* **search_terms:** The list of search terms to google image search
* **max_similtanous_threads:** The number of concurrent image fetches to execute
* **max_image_fetching_threads:** The number of concurrent image downloads to execute per image fetch
* **image_download_timeout:** The number of seconds to wait for an image to be downloaded before abandoning
* **total_images:** How many images you want downloaded for each of these search terms
* **headers:** Browser headers the library uses when making requests. Just use this example if you're not sure what to do. For more information go to https://urllib3.readthedocs.io
* **browser:** Browser object to fetch URL's from. This must be an instance of a Browser which takes browser type and the path to it's driver executable. For more information jump to the browser installation guides section

## Optional Arguments
* **extensions:** List of acceptable file extensions (default is jpg & png)
* **directories:** Names of folder to save images to (default is the same names as the search_terms)
* **progress_bar:** Whether to display a progress bar (default is True)
* **verbose:**Whether to print total downloaded & total ignored at the end (default is True)
