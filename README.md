# Python-Image-Fetcher (image_fetcher)

A simple lightweight library to download images from google.<br>
This is originally based on https://github.com/hardikvasa/google-images-download by hardikvasa but with a few key changes;

<ul>
  <li><b>Simplification:</b> Code has been simplified to make it more understandable and expandable</li>
  <li><b>Reduced download duplication:</b> By using the url from which the image was downloaded to name the file, we can avoid trying to redownload the same file in the future. This was a significant drawback with google_images_download as whenever you wanted to download images again it would redownload ones that already existed making it slower.</li>
  <li><b>Multithreading:</b> Implementing multithreading means you can run multiple google image downloads similtaneously massively increasing throughput when downloading a large selection of images</li>
  <li><b>Progress bar:</b> Added a tqdm progress bar to track how your download was getting on</li>
</ul>

## Table of Contents  
[Multi-Thread Multi-Search example](#multi-multi)  
[Multi-Thread Single-Search example](#multi-single)     


# Multi-Thread Examples
<a name="multi-multi"/>
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

<a name="multi-single"/>
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

# Performance considerations
Time in seconds to perform various image fetching tasks;
<table>
  <tr>
    <th>Task</th>
    <th><b>concurrent_image_search</b></th>
    <th><b>concurrent_images_download</b></th>
    <th><b>download_images</b></th>
  </tr>
  <tr>
    <td>Download 200 cat pictures</td>
    <td><b>23.6</b></td>
    <td><b>22.4</b></td>
    <td><b>92.7</b></td>
  </tr>
  <tr>
    <td>Download 200 cat & dog pictures</td>
    <td><b>28.7</b></td>
    <td><b>47.7</b></td>
    <td><b>254.2</b></td>
  </tr>
</table>
All tests were ran with the following config;
<ul>
  <li>total_images=200</li>
  <li>headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}</li>
  <li>progress_bar=False</li>
  <li>verbose=True</li>
</ul>
Both concurrent_image_search and concurrent_images_download were ran with;
<ul>
  <li>max_image_fetching_threads=20</li>
  <li>image_download_timeout=3</li>
</ul>
concurrent_image_search was also ran with max_similtanous_threads=2<br>

<b>Explanation;</b><br>
Understandably in all cases concurrent processing beat out single thread because they are able to download multiple images similtaneously. concurrent_image_search goes one step further with multiple search terms by running them similitaneoulsy, where the other 2 must run one after the other. What's interesting is that concurrent_image_search is slower than concurrent_images_download even though the first actually uses the second when executing. This delay is likely to do with the fact that concurrent_image_search must allocate the call to a thread handler, whereas concurrent_images_download starts immediatly.

<h2>How can you optimise performance?</h2>
Adjusting the following values will help improve your download speeds. Bear in mind however, that pushing these values too high may cause excessive strain on low performance machines. Adjust these at your own discretion.<br>
<ul>
  <li><b>max_image_fetching_threads:</b> This value states how many <b>similtaneous image fetching processes</b> can be executed. Increasing this value typically increases performance, but there is a tradeoff: If allocating too many threads the allocation time may actually take longer than fewer threads. In my tests at 200 images, I've found 20 to be roughly ideal, but play about with it and let me know what you find.</li>
  <li><b>image_download_timeout:</b> This value states how many seconds an image download will be <b>waited on before abandoning</b>. Decreasing this value will typically increase performance as it means slower downloads will be ignored, but bear in mind that if you set this value too low then too many images may be ignored and this will slow performance. It also means in this event more URL's will need to be fetched which is time consuming. I've found most images standard quality should be downloaded within 1-2 seconds, so typically use 3 for this value.</li>
  <li><b>max_similtanous_threads (concurrent_image_search only):</b> This value states how many <b>similatenous image search processes</b> can be executed. This is what makes this function more efficent for more searches at the same time (i.e. dogs & cats). For better preformance this value should be equal to how many search terms your making.</li>
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
