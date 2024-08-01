import csv

from typing import Any

import pandas as pd

from src.logger import setup_logging_reader_csv_xlsx

logger = setup_logging_reader_csv_xlsx()


def get_data_csv(file_path: str) -> list[dict[str, str]] | Any:
    """function convert csv-file to list of dictionaries"""
    try:
        with open(file_path, encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=";")
            logger.info("OK File read")
            return [row for row in data]
    except FileNotFoundError:
        logger.warning("Error File not Found")
        return []
    except csv.Error:
        logger.warning("Parser Error")
        return []


def get_data_xlsx(file_path: str) -> list[dict[str, str]] | Any:
    """function convert xlsx-file to list dictionaries"""
    try:
        df = pd.read_excel(file_path)
        data = df.to_dict(orient="records")
        logger.info("OK File read")
        return data
    except FileNotFoundError:
        logger.warning("Error File not Found")
        return []
    except pd.errors.ParserError:
        logger.warning("Parser Error")
        return []
