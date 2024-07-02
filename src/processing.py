from typing import Any

test_state = [
    {'id': 414288295, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(state_list: list[dict[str, Any]], state_value: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция фильтра списков словарей по ключу state"""
    new_list = []
    for state_dict in state_list:
        if state_dict['state'] == state_value:
            new_list.append(state_dict)
    return new_list






