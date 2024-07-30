import json

from src.logger import setup_logging_utils

logger = setup_logging_utils()


def json_to_list_dict(path_to_json_file):
    """Функция преобразования json-файла с данными в список словарей"""
    try:
        with open(path_to_json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        logger.warning("JSON-file read error")
        return []
    logger.info("JSON-file read ok")
    return data
