import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
from simulation import portfolio_simulations,var_99,var_95,final_values,initial_portfolio,num_simulations,returns,close_prices
plt.style.use('dark_background')

for i in range(num_simulations):
    plt.plot(portfolio_simulations[:,i],alpha = 0.01,color=plt.cm.plasma(i / num_simulations))
plt.title('Симуляция Монте-Карло — траектории портфеля')
plt.xlabel('Торговые дни')
plt.ylabel('Стоимость портфеля ($)')    
plt.show()

plt.figure()
plt.hist(final_values,bins=100, alpha = 0.7,color='yellow',)
plt.axvline(var_95,color = 'red',linewidth = 2, label = 'VaR 95%')
plt.axvline(var_99,color = 'orange',linewidth = 2, label = 'VaR 99%')
plt.legend()
plt.title('Распределение финальной стоимости портфеля')
plt.xlabel('Стоимость портфеля ($)')
plt.ylabel('Количество сценариев')
plt.show()

plt.figure()
sns.heatmap(returns.corr(),cmap='plasma',annot=True,fmt='.2f')
plt.title('Тепловая карта корреляции')
plt.show()

plt.figure()
for column in close_prices.columns:
    plt.plot(close_prices[column],label = column,)
    
plt.legend()
plt.title('График динамики реальных цен акций за 5 лет ')
plt.xlabel('Даты')
plt.ylabel('Цена акции в $')
plt.show()