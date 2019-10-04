# How to optimise performance
Adjusting the following values will help improve your download speeds. Bear in mind however, that pushing these values too high may cause excessive strain on low performance machines. Adjust these at your own discretion.


##max_image_fetching_threads 
This value states how many **similtaneous image fetching processes** can be executed. Increasing this value typically increases performance,but there is a tradeoff: If allocating too many threads the allocation time may actually take longer than fewer threads. In my tests at 200 images, I've found 20 to be roughly ideal, but play about with it and let me know what you find.

##image_download_timeout 
This value states how many seconds an image download will be **waited on before abandoning**. Decreasing this value will typically increase performance as it means slower downloads will be ignored, but bear in mind that if you set this value too low then too many images may be ignored and this will slow performance. It also means in this event more URL's will need to be fetched which is time consuming. I've found most standard quality images should be downloaded within 1-2 seconds, so typically use 3 for this value.

##max_similtanous_threads 
**concurrent_image_search only!**


This value states how many **similatenous image search processes** can be executed. This is what makes this function more efficent for more searches at the same time (i.e. dogs & cats). For better preformance this value should be equal to how many search terms your making.


##Why would I ever use single thread over multi?
Simply put it's marginally more reliable. The reason I say this is when you're executing multiple threads you increase the complexity and therefore slightly increase the risk of something going wrong. However in the vast majority of my tests I've had no thread-related issues so I wouldn't take concern with this, just treat single thread as a backup/alternative.
