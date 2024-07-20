import pytest

from src.widget import get_date, mask_account_card


def test_mask_account(new_acc_number):
    assert mask_account_card(new_acc_number) == "Счет **4305"


def test_mask_card(new_card_number):
    assert mask_account_card(new_card_number) == "Visa Platinum 7000 79** **** 6361"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет", None),
        ("Visa 1234123412341234", None),
        ("", None),
        ("MasterCard abcd792289606361", "MasterCard None"),
        ("12345123451234512345", None),
        ("1234123412341234", None),
        ("Maestro", None),
        ("Visa Classic 12341234123412345", "Visa Classic None"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_get_date(date):
    assert get_date(date) == "11.03.2024"
