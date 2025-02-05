import json
import requests

TOKEN = "2546734657:FESvGdvH3JsJvFdHt7-JBf-SEsFk4KnFT5f"

currencies = {
    'доллары': 'USD',
    'евры': 'EUR',
    'противные деньги': 'RUB',
    'нормальные деньги': 'BYN'
}


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if quote == base:
            raise APIException(f'Ебобо?: {base}.')

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        return json.loads(r.content)[quote_ticker]*amount
