import requests

from dotenv import load_dotenv

import os


def conversion_to_rub(currency, amount):
    """Функция конвертации валюты в рубли"""

    try:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        load_dotenv('../.env')
        apikey = os.getenv("API_KEY_EXCHANGE_RATES")
        headers = {"apikey": apikey}
        response = requests.get(url, headers=headers)
        result = response.json()
    except Exception as e:
        print(f"Error: {e}")
        return 0
    return round(result.get("result"), 2)


