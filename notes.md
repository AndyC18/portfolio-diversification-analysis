Initially, using the correlation over the entire time period it suggests that TLT and SPY have a negative correlation however after plotting the rolling correlation between TLT and SPY, it can be seen that leading up to 2022 correlation between the two rapidly increased to be positive and has sustained a correlation since, with 2026 reaching a new peak. Why is this?

Intersting findings from max drawdowns. TLT is a ticker that invests in long term US bonds and is supposedly low risk due to fixed return rates. In 2022, interest rates increased dramatically causing a huge sell off of bonds as they are stuck with a lower return percent which was the greatest max drawdown out of all four tickers. SPY and EFA had a similar max drawdown likely due to COVID-19 with a sharp crash but quick recovery compared  to TLTs slower crash but also slower recovery. 

From plotting drawdown against time, it can be seen that despite TLT being the least volatile compared to the equity tickers, it has an extremely slow recovery for the drawdown to return to 0 whereas SPY and EFA frequently peak new highs even if theres a lot more movement. This is arguably more dangerous than a deeper single crash that recovers quickly for investors who need money within a few years. under plotting_drawdown.py the time_underwater() function returns the days where drawdown was less than -10% giving:
EFA     844
GLD     952
SPY     407
TLT    2002

TLT clearly spends a significantly longer time recovering. Volatility treats up-moves and down-moves the same but says nothing about its displacement so while its not volatile (consistently returning a small negative %), it grinds down slowly over a long period of time.

covariance matrix - covariance is like correlation but not bounded from -1 to 1. It measures the jont variablity between two random variables. the matrix will be formed as AA,AB,BA,BB where each cell is the variation between the two variables. Where AA and BB is just the variance of that variable as its with itself and AB has the same covariance as BA. Its transpose is the matrix itself because its symmetric. to calculate the covariance of (A,B) its Exp(AB) - Exp(A)Exp(B)

findings from calculating portfolio volatility: when given equal weights between the 4 tickers and trained from 2015-2026, the volatility was 0.10343... compared to 0.165 had the volatilities been averaged out. this shows that diversification has decreased the volatility as if the correlation had been 1 between all tickets the volatility would have been 37% greater.

Things I've learnt doing this project:
implementing pandas, numpy, matoplotlib, seaborn into a practical project
how to use git and conventions such as git ignore
multiindexing using pandas
plotting heatmaps and graphs using matplot and seaborn
why bonds dont always hedge against commodities
why rolling windows are used rather than just one value for the entire window of time
why sd is proportional to root252 (variance proportional to time)
using PMCC
diversification
what maximum drawsum is and how to calculate it
how to calculate cumulative sum 
