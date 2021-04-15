import numpy as np
import pandas as pd

# 1차원 배열
a1 = np.array([1,2,3])
print(a1)

c = np.arange(15)
print(c)

c = c.reshape(3,5)
print(c)


prices = [1000, 1010, 1020]
dates = pd.date_range('20201120', periods=3)
print(dates)

s = pd.Series(prices, index=dates)
print(s)
