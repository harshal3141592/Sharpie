import yfinance as yf
import pandas as pd

def fetch_data(assets, start, end):
    data = yf.download(assets, start=start, end=end, auto_adjust=False)['Adj Close']

    if data.empty:
        raise ValueError("No data retrieved")

    if data.isnull().sum().sum() > 0:
        print("Warning: Missing data detected. Applying forward fill.")
        data = data.ffill()

    return data