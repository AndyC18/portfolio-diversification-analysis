import pandas as pd
import yfinance as yf

#header here tells pandas to use the first two rows as the headers, index_col the first column as the index. 
#when reading from csv it converted the top level column such as close to close1, close2.. etc for each ticker
#header here fixes this issue by telling pandas to use the first two rows as the headers

closePrices = pd.read_csv(filepath_or_buffer = 'data/raw/prices.csv', header=[0,1], index_col = 0, parse_dates = True) 
closePrices = closePrices['Close']
print(closePrices['EFA'].loc['2015-01-02':'2015-01-09'])
closePrices.to_csv('data/raw/close_prices.csv')