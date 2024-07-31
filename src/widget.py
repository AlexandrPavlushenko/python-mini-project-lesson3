from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(acc_card_number: str) -> str | None:
    """Функция общей маскировки карты и счета"""
    acc_card_list = str(acc_card_number).split(" ")
    if len(acc_card_list) == 2 and acc_card_list[0] == "Счет":
        return f"Счет {get_mask_account(acc_card_list[-1])}"
    elif len(acc_card_list) == 3 and acc_card_list[0] == "Visa":
        return f"Visa {acc_card_list[1]} {get_mask_card_number(acc_card_list[-1])}"
    elif len(acc_card_list) == 2 and acc_card_list[0] == "Visa":
        return f"{acc_card_list[0]} {get_mask_card_number(acc_card_list[-1])}"
    elif len(acc_card_list) == 2 and acc_card_list[0] == "Maestro":
        return f"{acc_card_list[0]} {get_mask_card_number(acc_card_list[-1])}"
    elif len(acc_card_list) == 2 and (acc_card_list[0]).lower() == "masterсard":
        return f"{acc_card_list[0]} {get_mask_card_number(acc_card_list[-1])}"
    else:
        return None


def get_date(g_data: str) -> str:
    """Функция преобразования даты"""
    if g_data[-1] == "Z":
        date_object = datetime.strptime(g_data, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = date_object.strftime("%d.%m.%Y")
    else:
        date_object = datetime.strptime(g_data, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date_object.strftime("%d.%m.%Y")
    return formatted_date
