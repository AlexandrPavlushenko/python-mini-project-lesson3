from src.utils import json_to_list_dict


def test_json_to_list_dict(sample_json_file):
    """Тестируем фуекцию json_to_list_dict"""
    result = json_to_list_dict(sample_json_file)
    expected = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    assert result == expected


def test_json_to_list_dict_empty(tmp_path):
    """Тестируем функцию с пустым JSON файлом"""
    json_file = tmp_path / "empty.json"
    with open(json_file, "w") as f:
        f.write("[]")

    result = json_to_list_dict(json_file)
    expected = []
    assert result == expected


def test_json_to_list_dict_invalid(tmp_path):
    """Тестируем функцию с некорректным JSON файлом"""
    json_file = tmp_path / "invalid.json"
    with open(json_file, "w") as f:
        f.write("{invalid json}")
    result = json_to_list_dict(json_file)
    expected = []
    assert result == expected
