from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"

html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs=BeautifulSoup(html, 'html.parser')

nameList=bs.findAll('span', {'class':'green'})

for name in nameList:
    print(name.get_text())

nameList=bs.findAll(text='the prince')
print(len(nameList))

