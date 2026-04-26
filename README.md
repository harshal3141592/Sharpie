
=======
### Sharpie: Portfolio Optimization Analysis using Monte Carlo Simulation ###

This project builds an optimized stock portfolio analysis using historical market data and Monte Carlo simulation to provide cumulative Sharpe Ratio for the entire portfolio.

## Features

* Fetches real stock data using Yahoo Finance
* Computes returns and covariance matrix
* Simulates 100,000+ portfolios
* Identifies optimal portfolio allocation
* Outputs expected return, volatility, and Sharpe ratio

## Concepts Used

* Modern Portfolio Theory
* Sharpe Ratio Optimization
* Monte Carlo Simulation

## Required Stuff

* Python
* Pandas
* NumPy
* yFinance

## Example Output

```
Expected Return: 18%
Volatility: 12%
Sharpe Ratio: 0.87
```

## How to Run

 ### Go to bash or .venv environment ###
``` bash
pip install -r requirements.txt
python main.py
```

### What I would love to  Improve/Add ###
* Portfolio constraints(get more contstraints like sentiments, regional news or random events for more accurate optimization)
* Backtesting
* Dashboard (Streamlit)

## Author
Harshal Hatzade
