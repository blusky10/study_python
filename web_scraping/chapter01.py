from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("Server could not be found")
    else:
        print("It worked")

    try:
        bs=BeautifulSoup(html.read(), 'html.parser')
        title=bs.body.h1
    except AttributeError as e:
        return None
    return title

title=getTitle("http://www.pythonscraping.com/pages/page1.html")

if title == None:
    print('title could not be found')
else:
    print(title)    
