def mask_account_card(acc_card_number: str) -> str | None:
    """Функция общей маскировки карты и счета"""

    import masks

    acc_card_list = acc_card_number.split(' ')
    if len(acc_card_list) == 2 and acc_card_list[0] == 'Счет':
        return f"Счет {masks.get_mask_account(acc_card_list[-1])}"
    elif len(acc_card_list) == 3 and acc_card_list[0] == 'Visa':
        return f"Visa {acc_card_list[1]} {masks.get_mask_card_number(acc_card_list[-1])}"
    elif len(acc_card_list) == 2 and acc_card_list[0] == 'Maestro' or acc_card_list[0] == 'MasterCard':
        return f"{acc_card_list[0]} {masks.get_mask_card_number(acc_card_list[-1])}"
    else:
        return None
