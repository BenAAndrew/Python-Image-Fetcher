# Chrome

## Download
Before downloading the chrome driver firstly check what version you have of chrome.

![alt text](https://github.com/BenAAndrew/Python-Image-Fetcher/raw/master/docs/images/chrome-about.PNG "Chrome about")

To do this go to ** Settings > Help > About Google Chrome **

![alt text](https://github.com/BenAAndrew/Python-Image-Fetcher/raw/master/docs/images/chrome-version.PNG "Chrome version")

In here make note of your version of chrome. Then go to 
[Chromedriver downloads](https://chromedriver.chromium.org/downloads "Chromedriver downloads") to get the correct version for you

## Setup
Once you've downloaded and extracted the driver move it into a directory of your choice. You can now define the browser object as below;
```
from image_fetcher.browsers import Browser, BrowserType

browser=Browser(BrowserType.CHROME, 'chromedriver')
```

Most examples in this guide place the driver in the same directory as the python file exectuing the code. 

If however you place it in another directory make sure to append it's path as follows like **'_path-to-chromedriver_/chromedriver'**

## Additional steps

### Windows
No additional steps. Just ensure your chromedriver ends with .exe like;
```
browser=Browser(BrowserType.CHROME, 'chromedriver.exe')
```

### MacOS
If you're on mac you might want to install chromdriver via brew alongside this download.
To install run
```
brew cask install chromedriver
```

Note this may not correspond with the version you need and so you may need to specify a version 
number or update your chrome.

### Linux
Run
```
sudo apt-get install chromium-chromedriver
```

And you can use 
```
/usr/lib/chromium-browser/chromedriver
```
as a path or save the driver locally to the same folder and just use 'chromedriver'
