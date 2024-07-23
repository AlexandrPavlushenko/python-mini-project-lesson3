import os

import requests

from dotenv import load_dotenv


def conversion_to_rub(currency, amount):
    """Функция конвертации валюты в рубли"""

    try:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        load_dotenv("../.env")
        apikey = os.getenv("API_KEY_EXCHANGE_RATES")
        headers = {"apikey": apikey}
        response = requests.get(url, headers=headers)
        result = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
    return round(result.get("result"), 2)


def transactions_amount(transactions):
    """Функция подсчитывает сумму транзакций в рублях
    c конвертацией валюты из USD и EUR"""
    total_amount = 0

    for transaction in transactions:
        if transaction == {}:
            continue

        currancy = transaction.get("operationAmount").get("currency").get("code")
        amount = transaction.get("operationAmount").get("amount")

        if currancy is None or amount is None:
            continue
        elif currancy == "RUB":
            total_amount += float(amount)
        elif currancy == "USD" or currancy == "EUR":
            amount_rub = conversion_to_rub(currancy, amount)
            total_amount += amount_rub
        else:
            continue
    return round(total_amount, 2)
