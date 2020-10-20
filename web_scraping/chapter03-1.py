from urllib.request import urlopen
from bs4 import BeautifulSoup

import re
import datetime
import random

import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"


html=urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs=BeautifulSoup(html, 'html.parser')

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    url = 'http://en.wikipedia.org{}'.format(articleUrl)
    html=urlopen(url)
    bs=BeautifulSoup(html, 'html.parser')    
    return bs.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links=getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    number=random.randint(0, len(links)-1)
    newArticle=links[number].attrs['href']
    
    print(newArticle)
    links=getLinks(newArticle)