import json

from external_api import conversion_to_rub


def transaction_data(path_to_json_file):
    """Функция преобразования json-файла с данными о транзакциях в список словарей"""
    try:
        with open(path_to_json_file, "r", encoding="utf-8") as file:
            content = json.load(file)
    except Exception:
        return []
    return content


def transactions_amount(transactions):
    """Функция подсчитывает сумму транзакций в рублях с конвертацией валюты"""
    total_amount = 0
    for transaction in transactions:
        currancy = transaction.get("operationAmount").get("currency").get("code")
        amount = float(transaction.get("operationAmount").get("amount"))
        if currancy == "RUB":
            total_amount += amount
        else:
            amount_rub = conversion_to_rub(currancy, amount)
            total_amount += amount_rub
    return total_amount


#  path = r"D:\My_Project\My_Python_Project\data\operations.json"
