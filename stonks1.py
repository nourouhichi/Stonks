#!/usr/bin/python3
import requests
from datetime import datetime
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

"""load data here"""
api_key = "c0v78b748v6pr2p77hmg"
symbol = "AAPL"
initial_timestamp = "1605543327"
end_timestamp = "1605629727"
url = 'https://finnhub.io/api/v1/indicator?symbol={}&resolution=1&from={}&to={}&nbdevup=2&nbdevdn=2&timeperiod=20&i&indicator=bbands&token={}'.format(
    symbol, initial_timestamp, end_timestamp, api_key)
res = requests.get(url)
data= json.dumps(res.json())

"""store data in dataframe"""
df = pd.read_json(data)
df = df.set_index('t')
df = df.drop(df.index [ [i for i in range(0,20) ] ])
df = df.rename(columns={'c': 'Closing Price'})
df = df.rename(columns={'middleband': 'SMA 20'})

"""converting timestamp to datetime format"""
timestamp_list=[]
for index in df.index:
    timestamp_list.append(datetime.fromtimestamp(index))
df.index = timestamp_list
print(df)

"""visualize data"""
plt.style.use('grayscale')
ax = df[['Closing Price','upperband','lowerband','SMA 20']].plot(color=["red", "darkgray", "darkgray", "blue"])
x_axis = df.index.get_level_values(0)
ax.fill_between(x_axis, df['upperband'], df['lowerband'], color='gainsboro')
plt.xlabel('Timestamp')
plt.ylabel('Price USD ($)')
plt.title('Bollinger Bands')
plt.show()
