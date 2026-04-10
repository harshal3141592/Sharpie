import numpy as np

def calculate_metrics(data):
    daily_returns = data.pct_change().dropna()

    mean_returns = daily_returns.mean() * 252
    cov_matrix = daily_returns.cov() * 252

    return mean_returns, cov_matrix


def monte_carlo_optimization(mean_returns, cov_matrix, num_portfolios=100000, risk_free_rate=0.075):
    num_assets = len(mean_returns)
    results = np.zeros((3 + num_assets, num_portfolios))

    for i in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)

        portfolio_return = np.dot(weights, mean_returns)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

        results[0, i] = portfolio_return
        results[1, i] = portfolio_volatility
        results[2, i] = sharpe_ratio
        results[3:, i] = weights

    return results