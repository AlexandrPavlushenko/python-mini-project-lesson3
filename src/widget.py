from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(acc_card_number: str) -> str | None:
    """Функция общей маскировки карты и счета"""
    acc_card_list = acc_card_number.split(" ")
    if len(acc_card_list) == 2 and acc_card_list[0] == "Счет":
        return f"Счет {get_mask_account(acc_card_list[-1])}"
    elif len(acc_card_list) == 3 and acc_card_list[0] == "Visa":
        return f"Visa {acc_card_list[1]} {get_mask_card_number(acc_card_list[-1])}"
    elif len(acc_card_list) == 2 and acc_card_list[0] == "Maestro" or acc_card_list[0] == "MasterCard":
        return f"{acc_card_list[0]} {get_mask_card_number(acc_card_list[-1])}"
    else:
        return None


def get_date(g_data: str) -> str:
    """Функция преобразования даты"""
    return f"{g_data[8:10]}.{g_data[5:7]}.{g_data[0:4]}"
