# Python-Image-Fetcher (image_fetcher)

A simple lightweight library to download images from google.<br>
This is originally based on https://github.com/hardikvasa/google-images-download by hardikvasa but with a few key changes;

<ul>
  <li><b>Simplification:</b> Code has been simplified to make it more understandable and expandable</li>
  <li><b>Reduced download duplication:</b> By using the url from which the image was downloaded to name the file, we can avoid trying to redownload the same file in the future. This was a significant drawback with google_images_download as whenever you wanted to download images again it would redownload ones that already existed making it slower.</li>
  <li><b>Multithreading:</b> Implementing multithreading means you can run multiple google image downloads similtaneously massively increasing throughput when downloading a large selection of images</li>
  <li><b>Progress bar:</b> Added a tqdm progress bar to track how your download was getting on</li>
</ul>
