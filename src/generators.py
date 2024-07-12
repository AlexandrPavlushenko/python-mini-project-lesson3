def filter_by_currency(transactions, currency):
    """Функция возращает итератор транзакций по ключу currency"""
    filtered_transactions = list(
        filter(
            lambda transaction: transaction.get("operationAmount").get("currency").get("code") == currency,
            transactions,
        )
    )
    if len(filtered_transactions) != 0:
        yield filtered_transactions
    else:
        return []


def transaction_descriptions(transactions):
    """Функция принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, stop):
    """Генератор номеров карт в заданном параметре"""

    for number in range(start, stop + 1):
        number_str = f"{number:016}"
        formatted_number = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
        yield formatted_number
