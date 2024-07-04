import pytest


@pytest.fixture
def card_number():
    return '7000792289606361'


@pytest.fixture
def acc_number():
    return '73654108430135874305'


@pytest.fixture
def new_acc_number():
    return 'Счет 73654108430135874305'


@pytest.fixture
def new_card_number():
    return 'Visa Platinum 7000792289606361'


@pytest.fixture
def date():
    return '2024-03-11T02:26:18.671407'
