import requests

class Model:
    CRYPTO_NAME_TO_TICKER = {
        "Bitcoin": "BTCUSDT",
        "Ethereum": "ETHUSDT",
        "Toncoin": "TONUSDT"
    }

    #Парсинг цін на криптовалюту з API Binance.
    def get_price_by_ticker(self, ticker: str) -> float:
        endpoint = "https://api.binance.com/api/v3/ticker/price"
        params = {'symbol': ticker}
        response = requests.get(endpoint, params=params)
        data = response.json()
        price = round(float(data['price']), 2)
        return price
