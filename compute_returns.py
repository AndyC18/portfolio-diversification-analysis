import pandas as pd
import numpy as np
from fetch_close_prices import load_close_prices

def compute_log_returns_closed():
    close_prices = load_close_prices()
    return np.log(close_prices / close_prices.shift(1)).dropna()


    
    