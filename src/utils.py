import json


def transaction_data(path_to_json_file: str) -> list[dict]:
    """Функция преобразования json-файла с данными о транзакциях в список словарей"""
    try:
        with open(path_to_json_file, 'r', encoding='utf-8') as file:
            content = json.load(file)
    except Exception:
        return []
    return content

#  path = r"D:\My_Project\My_Python_Project\data\operations.json"

