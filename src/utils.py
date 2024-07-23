import json


def json_to_list_dict(path_to_json_file):
    """Функция преобразования json-файла с данными в список словарей"""
    try:
        with open(path_to_json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    return data
