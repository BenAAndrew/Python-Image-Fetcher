# FAQ's
##How do I change browser type 
As explained in the **browser installation guides** section you need to define the Browser
object that is passed to the image search once you have downloaded the corresponsing driver. 
This takes the browser type and path to the driver. For Chrome this would be
```
from image_fetcher.browsers import Browser, BrowserType
Browser(BrowserType.CHROME, 'chromedriver')
```
for using chrome where the chromedriver was in the same directory as the python file. Or
```
from image_fetcher.browsers import Browser, BrowserType
Browser(BrowserType.FIREFOX, 'geckodriver')
```
for firefox where geckodriver is in the same directory. Also ensure you have the file extension 
(i.e. .exe on the end of the driver path for windows like `chromedriver.exe`)

##When should I use each method
* **Multi-thread Multi-search:** Use this method when trying to fetch from multiple search terms similtaneously. 
This would be the most widely used function, particually for generating large datasets quickly.

* **Multi-thread Single-search:** Very similar to the one above except only takes a single search term. Use this
when you want to fetch images of only one search term (i.e. 'dogs') rather than a list of terms (i.e. ['dogs','cats'])

* **Single-thread Single-search:** A backup version of the method above. Doesn't implement multithreading making it
slower, but is also less complicated and therefore slightly reduces the chance of error. However I wouldn't recommend using this unless
you cannot use one of the others for some reason. 


##How do I improve performance
Head over to [Optimising performance](https://python-image-fetcher.readthedocs.io/en/latest/Performance/How-to-optimise-performance/ "Optimise") for further details of how to improve download speeds
