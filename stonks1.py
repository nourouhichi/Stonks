#!/usr/bin/python3
import requests
from datetime import datetime
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""load data here"""
api_key = "c0v78b748v6pr2p77hmg"
symbol = "AAPL"
initial_timestamp = "1605543327"
end_timestamp = "1605629727"
url = 'https://finnhub.io/api/v1/indicator?symbol={}&resolution=1&from={}&to={}&nbdevup=2&nbdevdn=2&i&indicator=bbands&token={}'.format(
    symbol, initial_timestamp, end_timestamp, api_key)
res = requests.get(url)
data= json.dumps(res.json())

"""store data in dataframe"""
df = pd.read_json(data)
df = df.set_index('t')
df = df.drop(df.index [ [ 0,1 ] ])
df = df.rename(columns={'c': 'Closing price'})
print(df)

"""visualize data"""
ax = df[['Closing price','upperband','lowerband']].plot()
plt.xlabel('Timestamp')
plt.ylabel('Price USD ($)')
plt.title('Bollinger Bands')
plt.show()
