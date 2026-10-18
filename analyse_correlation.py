from compute_returns import compute_log_returns_closed
from fetch_close_prices import load_close_prices
import numpy as np
import pandas as pd

#calculates the correlation matrix of the log returns for SPY, GLD, TLT, and EFA. 
#The results show that treasuries (TLT) are negatively correlated with equities (SPY and EFA), while  being positively correlated with gold (GLD).
#GLD is close to moving independently to SPY and EFA, which is consistent with the fact that gold is often seen as a good diversifier for equity portfolios.
#The correlation between SPY and EFA is positive, which is expected since they are both equity ETFs.

#correlation over entire time period
def correlation_matrix():
    correlation_matrix = compute_log_returns_closed().corr()
    return correlation_matrix


#stores a 90 day rolling correlation between SPY and TLT, in the year 2022 it can be seen that the correlation changed drastically from
#negative to positive, challenging the notion that treasuries are a good hedge for equities.
#stored as a time series rather than a singular value 
def rolling_correlation_SPY_TLT():
    log_returns = compute_log_returns_closed()
    rolling_correlation_SPY_TLT = log_returns['SPY'].rolling(window = 90).corr(log_returns['TLT'])
    return rolling_correlation_SPY_TLT

print(correlation_matrix())

