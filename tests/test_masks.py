import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "value, expected", [("7000", None), ("70007922896063611", None), ("", None), ("abcd792289606361", None)]
)
def test_get_mask_card_numbers(value, expected):
    assert get_mask_card_number(value) == expected


def test_get_mask_account(acc_number):
    assert get_mask_account(acc_number) == "**4305"


@pytest.mark.parametrize(
    "value, expected", [("7365", None), ("736541084301358743055", None), ("", None), ("7365410843013587abcd", None)]
)
def test_get_mask_accounts(value, expected):
    assert get_mask_account(value) == expected
