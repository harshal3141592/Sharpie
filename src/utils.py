import numpy as np

def get_best_portfolio(results, assets):
    max_sharpe_idx = np.argmax(results[2])

    best_weights = results[3:, max_sharpe_idx]
    best_return = results[0, max_sharpe_idx]
    best_volatility = results[1, max_sharpe_idx]
    best_sharpe = results[2, max_sharpe_idx]

    portfolio = dict(zip(assets, best_weights))

    return portfolio, best_return, best_volatility, best_sharpe