# Firefox

## Download
Firstly download geckodriver for your OS;
[Geckodriver releases](https://github.com/mozilla/geckodriver/releases "Geckodriver")

As far as I'm aware all versions of firefox are supported so I'd recommend downloading the latest version.

## Setup
As with chrome, most examples in this guide place the driver in the same directory as the python file exectuing the code. 

If however you place it in another directory make sure to append it's path as follows like **'_path-to-geckodriver_/geckodriver'**

```
from image_fetcher.browsers import Browser, BrowserType

browser=Browser(BrowserType.FIREFOX, 'geckodriver')
```

Also make sure to include it's file extension (i.e. .exe for windows)
