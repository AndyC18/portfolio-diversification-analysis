import pandas as pd
import yfinance as yf

list_of_tickers = ['SPY', 'EFA', 'GLD', 'TLT',]

data = yf.download(list_of_tickers, start='2015-01-01', end= '2026-08-21')

data.to_csv('data/raw/prices.csv')

