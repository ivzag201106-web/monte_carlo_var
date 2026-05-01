import pandas as pd
import yfinance as yf
def get_stock_data():
    tickers = ['AAPL', 'TSLA', 'GOOGL', 'AMZN', 'MSFT']
    start_date = '2021-05-01'
    end_date = '2026-05-01'
    data = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        group_by='ticker',
        auto_adjust=True,
        progress=False )
    close_price= data.xs('Close',axis=1,level='Price')
    return close_price

