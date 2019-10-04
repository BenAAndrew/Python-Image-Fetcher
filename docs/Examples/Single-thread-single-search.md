# Single-Thread Single-Search
Use this method as a backup in case multithreading image searhces is causing you problems

## Quick Start
```
from image_fetcher.image_fetcher import download_images
from image_fetcher.browsers import Browser, BrowserType

download_images(
        search_term='Dog', 
        total_images=10,  
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'},
        browser=Browser(BrowserType.CHROME, 'chromedriver.exe')
    )
```

## Key arguments
* **search_term:** The search term to google image search
* **total_images:** How many images you want downloaded for each of these search terms
* **headers:** Browser headers the library uses when making requests. Just use this example if you're not sure what to do. For more information go to https://urllib3.readthedocs.io
* **browser:** Browser object to fetch URL's from. This must be an instance of a Browser which takes browser type and the path to it's driver executable. For more information jump to the browser installation guides section

## Optional Arguments
* **extensions:** List of acceptable file extensions (default is jpg & png)
* **directories:** Names of folder to save images to (default is the same names as the search_terms)
* **progress_bar:** Whether to display a progress bar (default is True)
* **verbose:**Whether to print total downloaded & total ignored at the end (default is True)