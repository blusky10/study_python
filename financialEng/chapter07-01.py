from urllib.request import urlopen

import datetime as dt
import bs4
import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"

index_cd = 'KPI200'
page_n = 1
naver_index = 'https://finance.naver.com/sise/sise_index_day.nhn?code=' + index_cd + '&page=' + str(page_n)


source = urlopen(naver_index).read()

source = bs4.BeautifulSoup(source, 'lxml')
print(source.find_all('table')[0].find_all('tr')[2].find_all('td')[0])


dates = source.find_all('td', class_='date')
prices = source.find_all('td', class_='number_1')


def date_format(d):
    d = str(d).replace('-','.')
    yyyy = int(d.split('.')[0])
    mm = int(d.split('.')[1])
    dd = int(d.split('.')[2])
    this_date = dt.date(yyyy,mm,dd)
    return this_date

for n in range(len(dates)):
    this_date = date_format(dates[n].text)
    this_close = prices[n*4].text
    this_close = this_close.replace(',', '')
    this_close = float(this_close)
    print(this_date, this_close)


