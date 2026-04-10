from src.data_loader import fetch_data
from src.optimizer import calculate_metrics, monte_carlo_optimization
from src.utils import get_best_portfolio


def get_user_inputs():
    print("Enter date range")
    start_date = input("Start date (YYYY-MM-DD): ").strip()
    end_date = input("End date (YYYY-MM-DD): ").strip()

    print("\n Enter stock tickers (comma-separated)")
    print("Example: RELIANCE.NS, TCS.NS, INFY.NS")
    tickers_input = input("Tickers: ").strip()

    assets = [ticker.strip().upper() for ticker in tickers_input.split(",")]

    if len(assets) < 2:
        raise ValueError("Please enter at least 2 tickers for diversification.")

    return assets, start_date, end_date


def main():
    try:
        assets, start_date, end_date = get_user_inputs()

        print("\n Fetching data...")
        data = fetch_data(assets, start_date, end_date)

        print("Running optimization...")
        mean_returns, cov_matrix = calculate_metrics(data)

        results = monte_carlo_optimization(mean_returns, cov_matrix)

        portfolio, ret, vol, sharpe = get_best_portfolio(results, assets)

        print("\n Optimized Portfolio:\n")
        for stock, weight in portfolio.items():
            print(f"{stock}: {weight:.4f}")

        print(f"\nExpected Return: {ret:.2%}")
        print(f"Volatility: {vol:.2%}")
        print(f"Sharpe Ratio: {sharpe:.2f}")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()