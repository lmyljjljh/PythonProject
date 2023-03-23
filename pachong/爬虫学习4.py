from urllib.parse import urlparse
from datetime import datetime
import time
import requests

class lmy1:
    def __init__(self,delay=3):
        self.delay = delay
        self.urls = {}
    def wait(self,url):
        netloc = urlparse(url).netloc
        print(netloc)
        lastOne = self.urls.get(netloc,False)
        if lastOne and self.delay > 0:
            sleepTime = self.delay - (datetime.now()-lastOne).seconds
            if sleepTime > 0:
                time.sleep(sleepTime)
        self.urls[netloc] = datetime.now()

if __name__ == '__main__':
    urls = ["https://github.com/"]*10
    d = lmy1()
    # d.wait(urls)
    for url in urls:
        html = requests.get(url)
        d.wait(url)
        print(html.status_code)

