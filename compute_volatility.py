from fetch_close_prices import load_close_prices
from compute_returns import compute_log_returns_closed
import pandas as pd
import numpy as np

def compute_volatility(trading_days_a_year =252):
    volatility = compute_log_returns_closed().std() * np.sqrt(trading_days_a_year)
    return volatility

#results suggest volatility goes SPY>EFA>GLD>TLT, which is consistent with the fact that SPY is an equity ETF, EFA is an international equity ETF, GLD is a gold ETF, and TLT is a long-term treasury ETF.
print(compute_volatility())

    