import pandas as pd
import yfinance as yf

list_of_tickers = ['SPY', 'EFA', 'GLD', 'TLT',]

data = yf.download(list_of_tickers, start='2015-01-01')

print(data.info())
print(data.head())

data.to_csv('data/raw/prices.csv')

