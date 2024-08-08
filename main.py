import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://www.alphavantage.co/query?'

# Portfolio dictionary to store stock symbol and shares
portfolio = {}

def get_stock_price(symbol):
    """
    Get the latest stock price for the given symbol from Alpha Vantage.
    """
    params = {
        'function': '',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEYTIME_SERIES_INTRADAY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    try:
        last_refreshed = data['Meta Data']['3. Last Refreshed']
        latest_price = float(data['Time Series (1min)'][last_refreshed]['1. open'])
        return latest_price
    except KeyError:
        print(f"Error retrieving data for {symbol}")
        return None

def add_stock(symbol, shares):
    """
    Add a stock to the portfolio.
    """
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares
    print(f"Added {shares} shares of {symbol} to portfolio.")

def remove_stock(symbol, shares):
    """
    Remove a stock from the portfolio.
    """
    if symbol in portfolio:
        if portfolio[symbol] > shares:
            portfolio[symbol] -= shares
            print(f"Removed {shares} shares of {symbol} from portfolio.")
        elif portfolio[symbol] == shares:
            del portfolio[symbol]
            print(f"Removed {symbol} from portfolio.")
        else:
            print(f"Not enough shares to remove. You have {portfolio[symbol]} shares of {symbol}.")
    else:
        print(f"{symbol} not found in portfolio.")

def track_portfolio():
    """
    Track the performance of the portfolio.
    """
    total_value = 0
    for symbol, shares in portfolio.items():
        price = get_stock_price(symbol)
        if price:
            value = shares * price
            total_value += value
            print(f"{symbol}: {shares} shares @ ${price:.2f} each = ${value:.2f}")
    print(f"Total portfolio value: ${total_value:.2f}")

def main():
    while True:
        print("\nPortfolio Tracker Menu:")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Track portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            remove_stock(symbol, shares)
        elif choice == '3':
            track_portfolio()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
