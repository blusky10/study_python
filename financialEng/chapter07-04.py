import pandas as pd

from urllib.request import urlopen
import json
import os
os.environ["HTTP_PROXY"] = "http://70.10.15.10:8080"
os.environ["HTTPS_PROXY"] = "http://70.10.15.10:8080"
os.environ["PYTHONHTTPSVERIFY"] = "0"


def date_fromat(d=''):
    if d != '':
        this_date = pd.to_datetime(d).date()
    else:
        this_date = pd.Timestamp.today().date()
    return (this_date)


def index_global(d, symbol, start_date='', end_date='', page=1):

    end_date = date_fromat(end_date)

    if start_date == '':
        start_date = end_date - pd.DateOffset(months=1)
    
    start_date = date_fromat(start_date)

    url = 'https://finance.naver.com/world/worldDayListJson.nhn?symbol=' + symbol + '&fdtc=0&page=' + str(page)
    raw = urlopen(url)
    data = json.load(raw)

    if len(data) > 0:
        for n in range(len(data)):
            date = pd.to_datetime(data[n]['xymd']).date()

            if date <= end_date and date >= start_date:
                price = float(data[n]['clos'])
                d[date] = price
            elif date < start_date:
                return (d)


    if len(data) == 10:
        page += 1
        index_global(d, symbol, start_date, end_date, page)

    return (d)

indices = {
    'SPI@SPX' : 'S&P 500',
    'NAS@NDX' : 'Nasdaq 100',
    'NII@NI225' : 'Nikkei 225',
}

historical_indices = dict()
start_date = '2020-11-01'
end_date = '2020-11-17'

for key, value in indices.items():
    s = dict()
    s = index_global(s, key, start_date)
    historical_indices[value] = s

prices_df = pd.DataFrame(historical_indices)
print(prices_df)
# # print(prices_df.tail(3))