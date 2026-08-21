import pandas as pd
import yfinance as yf

#header here tells pandas to use the first two rows as the headers, index_col the first column as the index.
#when reading from csv it converted the top level column such as close to close1, close2.. etc for each ticker
#header here fixes this issue by telling pandas to use the first two rows as the headers

def load_close_prices(filepath = 'data/clean/close_prices.csv'):
    return pd.read_csv(filepath, index_col = 0,  parse_dates = True)

def clean_and_save_close_prices():
    closePrices = pd.read_csv(filepath_or_buffer = 'data/raw/prices.csv' ,header=[0,1], index_col = 0, parse_dates = True)
    closePrices = closePrices['Close']
    closePrices.to_csv('data/clean/close_prices.csv')
    return closePrices


