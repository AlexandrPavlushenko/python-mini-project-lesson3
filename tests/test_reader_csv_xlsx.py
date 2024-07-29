import unittest

from unittest.mock import mock_open, patch

from src.reader_csv_xlsx import get_data_csv, get_data_xlsx

import pandas as pd


class TestGetDataCsv(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="id;state;date;amount;currency_name;currency_code;from;to;"
        "description\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;"
        "PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n",
    )
    def test_get_data_csv(self, mock_file):
        expected_result = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        # Calling a function with a substituted file
        result = get_data_csv("fake_path.csv")

        self.assertEqual(result, expected_result)


class TestGetDataXlsx(unittest.TestCase):
    @patch("pandas.read_excel")
    def test_get_data_xlsx(self, mock_read_excel):
        # Создаем пример DataFrame, который мы ожидаем получить
        mock_data = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        mock_dataframe = pd.DataFrame(mock_data)
        mock_read_excel.return_value = mock_dataframe

        result = get_data_xlsx("fake_file.xlsx")

        # Ожидаемый результат
        expected_result = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        self.assertEqual(result, expected_result)

        mock_read_excel.assert_called_once_with("fake_file.xlsx")
