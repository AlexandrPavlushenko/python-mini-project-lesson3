from src.logger import setup_logging_masks

logger = setup_logging_masks()


def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера карты"""
    if card_number.isdigit() and len(card_number) == 16:
        logger.info("The card number format is correct")
        return f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
    else:
        logger.warning("The card number format is invalid")
        return None


def get_mask_account(acc_number: str) -> str | None:
    """Функция маскировки номера счета"""
    if acc_number.isdigit() and len(acc_number) == 20:
        logger.info("Bank account number format is correct")
        return f"{'*' * 2}{acc_number[-4::]}"
    else:
        logger.warning("Bank account number format is invalid")
        return None
