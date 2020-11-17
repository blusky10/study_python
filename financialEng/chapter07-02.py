from urllib.request import urlopen

import datetime as dt
import bs4
import os
os.environ["HTTP_PROXY"] = "http://70.10.15.10:8080"
os.environ["HTTPS_PROXY"] = "http://70.10.15.10:8080"
os.environ["PYTHONHTTPSVERIFY"] = "0"

def date_format(d):
    d = str(d).replace('-','.')
    yyyy = int(d.split('.')[0])
    mm = int(d.split('.')[1])
    dd = int(d.split('.')[2])
    this_date = dt.date(yyyy,mm,dd)
    return this_date

def historical_index_naver(index_cd, start_date, end_date, page_n=1, last_page=0):

    if start_date:
        start_date = date_format(start_date)
    else:
        start_date = dt.date.today()

    if end_date:
        end_date = date_format(end_date)
    else:
        end_date = dt.date.today()        

    naver_index = 'https://finance.naver.com/sise/sise_index_day.nhn?code=' + index_cd + '&page=' + str(page_n)

    source = urlopen(naver_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')
    
    dates = source.find_all('td', class_='date')
    prices = source.find_all('td', class_='number_1')

    for n in range(len(dates)):

        this_date = date_format(dates[n].text)

        if this_date <= end_date and this_date >= start_date:
            this_close = prices[n*4].text
            this_close = this_close.replace(',', '')
            this_close = float(this_close)
            historical_prices[this_date] = this_close
        elif this_date < start_date:
            return historical_prices

    if last_page == 0:
        last_page = source.find('td', class_='pgRR').find('a')['href']
                
        last_page = last_page.split('&')[1]
        last_page = last_page.split('=')[1]
        last_page = int(last_page)

    if page_n < last_page:
        page_n = page_n + 1
        historical_index_naver(index_cd, start_date, end_date, pange_n, last_page)
    
    return historical_prices



index_cd = 'KPI200'
historical_prices = dict()
historical_prices = historical_index_naver(index_cd, '2020-11-11', '2020-11-12')
print(historical_prices)
