
from compute_returns import compute_log_returns_closed
import numpy as np

#gets the cumulative return up to every date
def compute_cum_return():
    log_returns = compute_log_returns_closed()
    cum_return_log = log_returns.cumsum()
    growth_multiple = np.exp(cum_return_log)
    return growth_multiple

#running max stores the max cumulative return up to that date
#drawdown calculates how far the returns have fallen as a percentage relative to previous peak
def compute_drawdown():
    cum_returns = compute_cum_return()
    running_max = cum_returns.cummax()
    drawdown = (cum_returns - running_max) / running_max
    return drawdown
    
#calculates the max drawdown
def compute_max_drawdown():
    drawdown = compute_drawdown()
    max_drawdown = drawdown.min()
    return max_drawdown
    
#-10% drawdown
def time_underwater():
    drawdown = compute_drawdown()
    return drawdown.where(drawdown <= -0.1).count()
    
print(time_underwater())
# print(compute_cum_return())
# print(compute_max_drawdown())