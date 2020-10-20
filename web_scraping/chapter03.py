from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"


html=urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs=BeautifulSoup(html, 'html.parser')

for link in bs.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])