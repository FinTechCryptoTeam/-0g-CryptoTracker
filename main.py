import requests

def get_crypto_price(ticker):
    url = f"https://api.coinmarketcap.com/v1/ticker/{ticker}/"
    response = requests.get(url)
    data = response.json()
    return data[0]['price_usd']

if __name__ == "__main__":
    ticker = 'bitcoin'
    price = get_crypto_price(ticker)
    print(f"The current price of {ticker} is: ${price}")
