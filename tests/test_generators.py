from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(list_transactions):
    assert next(filter_by_currency(list_transactions, "RUB")) == [
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 74489636417521191160",
        },
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_transaction_descriptions():
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
    ]

    descriptions = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    assert descriptions == expected


def test_card_number_generator():
    generator = card_number_generator(1, 7)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
    assert next(generator) == "0000 0000 0000 0006"
    assert next(generator) == "0000 0000 0000 0007"
