#/Library/Frameworks/Python.framework/Versions/3.6/bin

import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()

df = web.DataReader("XOM", "morningstar", start, end)

print(df.head())

df.reset_index(inplace=True)
df.set_index("Date",inplace=True)
df = df.drop("Symbol",axis=1)

print(df.head())

style.use("fivethirtyeight")

df['High'].plot()
plt.legend()
plt.show()
