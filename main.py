import os

from src.utils import json_to_list_dict

from src.reader_csv_xlsx import get_data_csv, get_data_xlsx

from src.processing import filter_by_state, sort_by_date

from src.search_transactions import filter_transactions

from src.widget import mask_account_card, get_date


def main() -> None:
    """Функция отвечает за основную логику проекта и связывает функциональности между собой."""
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")
    path = os.path.dirname(os.path.abspath(__file__))
    while True:
        number_file = input()
        if number_file.isdigit() and 1 <= int(number_file) <= 3:
            break
    if int(number_file) == 1:
        data_list = json_to_list_dict(os.path.join(path, r"data\operations.json"))
    elif int(number_file) == 2:
        data_list = get_data_csv(os.path.join(path, r"data\transactions.csv"))
    else:
        data_list = get_data_xlsx(os.path.join(path, r"data\transactions_excel.xlsx"))
    print("""\nВведите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    while True:
        status_filter = input()
        if status_filter.upper() in ["CANCELED", "PENDING", "EXECUTED"]:
            break
        else:
            print(f"Статус операции {status_filter} недоступен.")
            continue
    data_filtered = filter_by_state(data_list, state_value=status_filter.upper())

    print("\nОтсортировать операции по дате? Да/Нет")
    while True:
        filter_by_date = input()
        if filter_by_date.lower() == "да":
            print("\nОтсортировать по возрастанию или по убыванию?")
            reverse = input()
            if reverse.lower() == "по убыванию":
                reverse_date = True
            else:
                reverse_date = False
            data_filtered = sort_by_date(data_filtered, reverse_date=reverse_date)
            break
        elif filter_by_date.lower() == "нет":
            break
        else:
            continue

    print("\nВыводить только рублевые тразакции? Да/Нет")
    while True:
        data_rub = input()
        if data_rub.lower() == "да" and int(number_file) == 1:
            data_filtered = list(
                filter(lambda x: x.get("operationAmount").get("currency").get("code") == "RUB", data_filtered))
            break
        elif data_rub.lower() == "да" and int(number_file) == 2:
            data_filtered = list(filter(lambda x: x.get("currency_code") == "RUB", data_filtered))
            break
        elif data_rub.lower() == "да" and int(number_file) == 3:
            data_filtered = list(filter(lambda x: x.get("currency_code") == "RUB", data_filtered))
            break
        elif data_rub.lower() == "нет":
            break
        else:
            continue

    print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
    while True:
        filter_by_word = input()
        if filter_by_word.lower() == "да":
            print("\nВведите слово")
            word = input()
            data_filtered = filter_transactions(data_filtered, word)
            break
        if filter_by_word.lower() == "нет":
            break
        else:
            continue

    print("\nРаспечатываю итоговый список транзакций...")
    if not data_filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(data_filtered)}\n")
        for transaction in data_filtered:
            date = get_date(transaction.get("date"))
            print(f"{date} {transaction.get("description")}")
            account_from = ""
            if transaction.get("from"):
                account_from = (mask_account_card(transaction.get("from")))
            account_to = mask_account_card(transaction.get("to"))
            print(account_from, " -> ", account_to)
            if int(number_file) == 2 or int(number_file) == 3:
                amount = transaction.get("amount")
                name = transaction.get("currency_name")
            else:
                amount = transaction.get("operationAmount").get("amount")
                name = transaction.get("operationAmount").get("currency").get("name")
            print(f"Сумма: {amount} {name}\n")


if __name__ == "__main__":
    main()
