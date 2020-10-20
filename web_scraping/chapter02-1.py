from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"

import re

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bs=BeautifulSoup(html, 'html.parser')

# text=bs.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
# print(text)

images=bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})

for image in images:
    print(image['src'])
