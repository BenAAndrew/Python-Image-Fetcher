# Timing Results
Time in seconds to perform various image fetching tasks;
<table>
  <tr>
    <th>Task</th>
    <th><b>Multi-thread multi-search (concurrent_image_search)</b></th>
    <th><b>Multi-thread single-search (concurrent_images_download)</b></th>
    <th><b>Single-thread single-search (download_images)</b></th>
    <th><b>google-images-download by hardikvasa</b></th>
  </tr>
  <tr>
    <td>Download 200 cat pictures</td>
    <td><b>23.6</b></td>
    <td><b>22.4</b></td>
    <td><b>92.7</b></td>
    <td><b>148.4</b></td>
  </tr>
  <tr>
    <td>Download 200 cat & dog pictures</td>
    <td><b>28.7</b></td>
    <td><b>47.7</b></td>
    <td><b>254.2</b></td>
    <td><b>330.4</b></td>
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

google-images-download was ran with the following config;
arguments = {"keywords":"cat", "limit":200, "chromedriver": "chromedriver.exe", "format": "jpg", "print_urls":False}

##Explanation
Understandably in all cases concurrent processing beat out single thread because they are able to download multiple images similtaneously. concurrent_image_search goes one step further with multiple search terms by running them similitaneoulsy, where the other 2 must run one after the other. What's interesting is that concurrent_image_search is slower than concurrent_images_download even though the first actually uses the second when executing. This delay is likely to do with the fact that concurrent_image_search must allocate the call to a thread handler, whereas concurrent_images_download starts immediatly.