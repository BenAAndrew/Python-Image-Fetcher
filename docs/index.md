# Home

**A simple lightweight library to download images from google.**
```
pip install image-fetcher
```


This is originally based on https://github.com/hardikvasa/google-images-download by hardikvasa but with a few major changes;

## Key features

* **Speed:** Through tests outlined in the 'Performance Considerations' section using this library is over **6x faster!**
* **Simplification:** Code has been simplified to make it more understandable and expandable
* **Reduced download duplication:** By using the url from which the image was downloaded to name the file, we can avoid trying to redownload the same file in the future. This was a significant drawback with google_images_download as whenever you wanted to download images again it would redownload ones that already existed making it slower.
* **Multithreading:** Implementing multithreading means you can run multiple google image downloads similtaneously massively increasing throughput when downloading a large selection of images
* **Extended browser support:** Added Firefox support and further configurations to come
* **Progress bar:** Added a tqdm progress bar to track how your download was getting on
