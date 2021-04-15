from urllib.request import urlopen

import datetime as dt
import bs4 

page_n = 1
category_id = '584df8ed-6dd0-4a38-bed2-1d746c116b38'
               
url = 'https://store.playstation.com/ko-kr/category/' + category_id + '/' + str(page_n)

source = urlopen(url).read()
source = bs4.BeautifulSoup(source, 'html.parser')

titles = source.find_all('span', class_='body-2 truncate-text-2 psw-p-t-2xs')
# discountRates = source.find_all('span', class_='body-2 discount-badge discount-badge--undefined')
# discountPrices = source.find_all('span', class_='price')
# orgPrices = source.find_all('strike', class_='price price--strikethrough')

print(titles)
# data = dict()
# for n in range(len(titles)):
#     title = titles[n].text
#     discountRate = discountRates[n].text
#     discountPrice = discountPrices[n].text
#     orgPrice = orgPrices[n].text
#     data[title] = {
#         'discountRate' : discountRate,
#         'discountPrice' : discountPrice,
#         'orgPrice' : orgPrice
#     }


# print(data)


# next_button = source.find_all('button', class_='ems-sdk-grid-paginator__button')

# print(next_button)
# <button data-qa="ems-sdk-grid-paginator-next-page-btn" id="" class="ems-sdk-grid-paginator__button psw-button psw-primary-button psw-content-button" aria-label="다음 페이지로 가기" type="button" name="" value="">


# <button data-qa="ems-sdk-grid-paginator-next-page-btn" id="" class="ems-sdk-grid-paginator__button psw-button psw-is-disabled psw-primary-button psw-content-button" aria-label="다음 페이지로 가기" type="button" name="" value="" disabled="">

