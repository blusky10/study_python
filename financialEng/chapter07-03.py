import pandas as pd

from urllib.request import urlopen
import json
import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"

def read_json(d, symbol, page=1):
    url = 'https://finance.naver.com/world/worldDayListJson.nhn?symbol=' + symbol + '&fdtc=0&page=' + str(page)
    raw = urlopen(url)
    data = json.load(raw)

    for n in range(len(data)):
        date = pd.to_datetime(data[n]['xymd']).date()
        price = float(data[n]['clos'])
        d[date] = price

    if len(data) == 10:
        page += 1
        read_json(d, symbol, page)

    return (d)

symbol = 'SPI@SPX'
page = 1

historical_index = pd.Series()
historical_index = read_json(historical_index, symbol, page)

print(historical_index.head(3))

indices = {
    'SPI@SPX' : 'S&P 500',
    'NAS@NDX' : 'Nasdaq 100',
    'NII@NI225' : 'Nikkei 225',
}

historical_indices = dict()

for key, value in indices.items():
    print(key, value)
    s = dict()
    s = read_json(s, key, 1)
    historical_indices[value] = s

prices_df = pd.DataFrame(historical_indices)
print(prices_df)