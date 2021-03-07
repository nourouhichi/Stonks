#!/usr/bin/python3


def import_data():
    """Requesting data from api"""
    import requests
    from datetime import datetime
    import json
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    plt.style.use("fivethirtyeight")

    """load data here"""
    api_key = "c122fkn48v6p2grllu60"
    symbol = "AAPL"
    initial_timestamp = "1605543327"
    end_timestamp = "1605629727"
    url = "https://finnhub.io/api/v1/stock/candle?symbol={}&resolution=1&from={}&to={}&token={}".format(
        symbol, initial_timestamp, end_timestamp, api_key)
    res = requests.get(url)
    #print(res.json())
    #print(type(res.json()))
    data = json.dumps(res.json())
    """store data in dataframe"""
    df = pd.read_json(data)
    df = df.set_index('t')
    print(df)
    """visualize data"""
    #plt.figure(figsize=(12.2,4.5))
    plt.plot(df['c'],label='Closing pricing')
    plt.title('close Price History')
    plt.xlabel('Timestamp')
    plt.ylabel('Price USD ($)')
    plt.show()

def strategy(capital, df):
    """ """"
    

def main():
    capital = input("Enter the capital: ")
    df = import_data()
    signal = strategy(capital, df)
