# Python-Image-Fetcher (image_fetcher)

A simple lightweight library to download images from google.<br>
This is originally based on https://github.com/hardikvasa/google-images-download by hardikvasa but with a few key changes;

<ul>
  <li><b>Simplification:</b> Code has been simplified to make it more understandable and expandable</li>
  <li><b>Reduced download duplication:</b> By using the url from which the image was downloaded to name the file, we can avoid trying to redownload the same file in the future. This was a significant drawback with google_images_download as whenever you wanted to download images again it would redownload ones that already existed making it slower.</li>
  <li><b>Multithreading:</b> Implementing multithreading means you can run multiple google image downloads similtaneously massively increasing throughput when downloading a large selection of images</li>
  <li><b>Progress bar:</b> Added a tqdm progress bar to track how your download was getting on</li>
</ul>

# Examples

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

Other examples;
```
from image_fetcher import download_images

download_images(
        search_term='Duck', 
        total_images=10,  
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'},
        extensions=['png'],
        directory='My duck photos'
    )
```
Would download images from the search 'Duck' to a folder called 'My duck photos' where the file type was 'png'
