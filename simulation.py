import pandas as pd
import numpy as np
from data_loading import get_stock_data
close_prices = get_stock_data()
returns = close_prices.pct_change().dropna()
num_simulations = 10000
num_days = 252
initial_portfolio = 100000
mean_returns = returns.mean()
cov_returns = returns.cov()
weight = np.array([0.2,0.2,0.2,0.2,0.2],dtype=float,)
portfolio_simulations = np.zeros((num_days, num_simulations))
for i in range(num_simulations):
    daily_returns = np.random.multivariate_normal(mean_returns,cov_returns,num_days)@weight
    portfolio_values = np.cumprod(1+daily_returns)*initial_portfolio
    portfolio_simulations[:, i] = portfolio_values
final_values = portfolio_simulations[-1, :]
var_95 = np.percentile(final_values, 5)
var_99 = np.percentile(final_values, 1)
volatility = np.std(final_values)
k_sharp = mean_returns.mean()/volatility.mean()*252
print('Волатильность равна',volatility)
print(f'Коэфициент Шарпа равен {k_sharp:.6f}')
print(f'VaR 95%: с вероятностью 95% потери не превысят {initial_portfolio - var_95:.2f}$')
print(f'VaR 99%: с вероятностью 99% потери не превысят {initial_portfolio - var_99:.2f}$')
