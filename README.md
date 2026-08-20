Research Question: Does diversification across different asset classes actually reduce the risk in a portfolio compared to a concentrated equity portfolio?

Rather than just investigating if a concentrated equity portfolio can return higher raw returns, this project questions whether combining different assets (specifically comodities, equities and bonds) improves risk-adjusted returns and the extent to which it is driven by their returns being uncorrelated. This involves analysing how volatility and drawdowns change. 

Motivation:
Diversification is a crucial element to investing and can result in massive differences in returns and volatility when different approaches are taken. This project is designed to see how big a difference diversification can make in a portfolio and to find that balance where risk is optimally reduced while not sacrificing too much potential income. Not only this but to test how the benefits of diversification holds in unconventional economic environments. For example, the inflation and interest rate shock in 2022 is an interesting test case as equities as well as government bonds experienced significant pressure, which opposes the usual assumption that bonds are always a safety net for when  equities fall.

Assets Used:
SPY - ETF consisting of US equities
EFA - International developed equities
TLT - long-term US treasuries
GLD - gold (commodities)

Data Source:
Daily historical market data will be taken from Yahoo Finance using the yfinance python library. For this project, data will be obtained covering 2015-2026. This provides access to historical Yahoo Finance market data and allows for downloading daily observations for multiple ticker symbols. The data is adjusted for dividends so that the findings are not skewed and reflect the investors actual total return.

Methodology:
1. Collect daily price data (2015–2026) for all four assets
2. Clean and align data across assets (handle missing days, compute returns)
3. Calculate historical volatility, correlation, and rolling correlation between asset classes
4. Construct portfolios under different allocations and compute portfolio-level risk/return
5. Evaluate risk-adjusted performance (Sharpe ratio, maximum drawdown)
6. Split data into in-sample (2015–2021) and out-of-sample (2022–2026) periods to test whether an allocation optimized on past data holds up on unseen data
7. Analyse performance specifically during major market shocks (2018, 2020, 2022)

Data:
Raw price data is incluced in 'data/raw/prices.csv' for reproducibility as it is what has been used to get to the projects conclusion. It was collected via 'fetch_data.py' using yfinance on 21/08/2026, covering 2015-01-01 to 2026/08/20 for SPY, EFA, TLT and GLD.



