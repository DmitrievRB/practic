import requests
import json
from config import keys


class ConvertionExpeption(Exception):# Класс для вызова исключений при обработки
    pass


class APIException: # Класс для обработки исключений при ошибке пользователя
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExpeption(f" Одинаковые валюты {base} не конвертируются.")
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExpeption(f"Такой валюты как {base} нет \n Увидеть список всех доступных валют : /values ")
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExpeption(f"Такой валюты как {quote} нет \n Увидеть список всех доступных валют : /values ")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExpeption(f"Не правильно ввели количество {amount}")
        #  Строка для отправки запроса к API сайта с валютами
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = float(json.loads(r.content)[keys[base]]) # Парсинг ответов json
        return total_base