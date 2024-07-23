from unittest.mock import patch

from src.external_api import conversion_to_rub, transactions_amount


@patch("requests.get")
def test_conversion_to_rub(mock_get):
    """Tест обработки API запроса функцией conversion_to_rub"""
    mock_get.return_value.json.return_value = {
        "date": "2024-07-23",
        "historical": True,
        "info": {"rate": 87.30041, "timestamp": 1721728444},
        "query": {"amount": 5, "from": "USD", "to": "RUB"},
        "result": 436.50205,
        "success": True,
    }
    assert conversion_to_rub("USD", 5) == 436.5


def test_transaction_amount(list_dict):
    """Тест обработки списка транзакций"""
    assert transactions_amount(list_dict) == 195936.45
