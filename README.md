# Python-Image-Fetcher (image_fetcher)

A simple lightweight library to download images from google.<br>
This is originally based on https://github.com/hardikvasa/google-images-download by hardikvasa but with a few key changes;

<ul>
  <li><b>Simplification:</b> Code has been simplified to make it more understandable and expandable</li>
  <li><b>Reduced download duplication:</b> By using the url from which the image was downloaded to name the file, we can avoid trying to redownload the same file in the future. This was a significant drawback with google_images_download as whenever you wanted to download images again it would redownload ones that already existed making it slower.</li>
  <li><b>Multithreading:</b> Implementing multithreading means you can run multiple google image downloads similtaneously massively increasing throughput when downloading a large selection of images</li>
  <li><b>Progress bar:</b> Added a tqdm progress bar to track how your download was getting on</li>
</ul>

# Multi-Thread Examples
<h2>Multiple search terms</h2>

Quick Start;
```
from multithread_image_fetching import concurrent_image_search

concurrent_image_search(
    search_terms=['cat','dog'], 
    max_similtanous_threads=2,
    max_image_fetching_threads=20,
    image_download_timeout=5,
    total_images=200, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
)
```
Key arguments;
<ul>
  <li><b>search_terms:</b> The list of search terms to google image search</li>
  <li><b>max_similtanous_threads:</b> The number of concurrent image fetches to execute</li>
  <li><b>max_image_fetching_threads:</b> The number of concurrent image downloads to execute per image fetch</li>
  <li><b>image_download_timeout:</b> The number of seconds to wait for an image to be downloaded before abandoning</li>
  <li><b>total_images:</b> How many images you want downloaded for each of these search terms</li>
  <li><b>headers:</b> Browser headers the library uses when making requests. Just use this example if you're not sure what to do. For more information go to https://urllib3.readthedocs.io</li>
</ul>

Optional Arguments;
<ul>
  <li><b>extensions:</b> List of acceptable file extensions (default is jpg & png)</li>
  <li><b>directories:</b> Names of folder to save images to (default is the same names as the search_terms)</li>
  <li><b>progress_bar:</b> Whether to display a progress bar (default is True)</li>
  <li><b>verbose:</b>Whether to print total downloaded & total ignored at the end (default is True)</li>
</ul>

<h2>Single search terms</h2>

Quick Start;
```
from multithread_image_fetching import concurrent_images_download

concurrent_images_download(
    search_term='cat', 
    max_image_fetching_threads=20,
    image_download_timeout=5,
    total_images=200, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
)
```
All arguments are the same as above except here search_terms is replaced with <b>search_term</b> as this function only accepts a single term and there is no <b>max_similtanous_threads</b> argument as we are only doing one google image search.

# Single-Thread Examples
For performance reasons outlined later I would reccommend using muti-threading. However if you choose not to this is how you would implement a single thread execution.

Quick Start;
```
from image_fetcher import download_images

download_images(
        search_term='Dog', 
        total_images=10,  
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    )
```
Key arguments;
<ul>
  <li><b>search_term:</b> The search term to google image search</li>
  <li><b>total_images:</b> How many images you want downloaded from this term</li>
  <li><b>headers:</b> Browser headers the library uses when making requests. Just use this example if you're not sure what to do. For more information go to https://urllib3.readthedocs.io</li>
</ul>

Optional Arguments;
<ul>
  <li><b>extensions:</b> List of acceptable file extensions (default is jpg & png)</li>
  <li><b>directory:</b> Name of folder to save images to (default is same name as the search_term)</li>
  <li><b>progress_bar:</b> Whether to display a progress bar (default is True)</li>
  <li><b>verbose:</b>Whether to print total downloaded & total ignored at the end (default is True)</li>
</ul>

# Other examples
```
...(
        search_term='Duck'
        ...
        extensions=['png'],
        directory='My duck photos'
    )
```
Would download images using your chosen function (concurrent_images_download or download_images) from the search 'Duck' to a folder called 'My duck photos' where the file type was 'png'

```
from image_fetcher import download_images

...(
        search_term='Ninja', 
        ...
        progress_bar=False
        verbose=False
    )
```
Would download images using your chosen function (concurrent_images_download or download_images) from the search 'Ninja' and hide the progress bar and summary text
