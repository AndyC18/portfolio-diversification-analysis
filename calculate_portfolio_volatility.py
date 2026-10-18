import numpy as np
from compute_returns import compute_log_returns_closed
#covariance matrix allows us to find the volatility of a portfolio given the weights of each asset in the portfolio. 
#covariance matrix = correlation matrix * volatility of each asset

def covariance_matrix():
    #we multiply by 252 because the .cov function is the covar for 1 day, scale by 252 for the year
    #tells us how they pairs of tickers move together. A large covariance tells us they move together
    #unlike correlation its not standardised and not bounded by |1|. cant compare across data sets
    #this doesnt account for weights, only how the relationship of how the raw data moves
    return compute_log_returns_closed().cov() * 252


def portfolio_volatility(weights, covarianceMatrix):
    
    portfolio_variance = covarianceMatrix.dot(weights).dot(np.transpose(weights))
    portfolioVolatility = np.sqrt(portfolio_variance)
    return portfolioVolatility


print(portfolio_volatility([0.25,0.25,0.25,0.25], covariance_matrix()))
