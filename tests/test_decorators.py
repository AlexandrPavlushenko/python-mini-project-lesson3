import tempfile

import pytest

from src.decorators import log, my_function


def test_log_good(capsys):
    """Тест выполнения декорированной функции"""

    @log()
    def func(x, y):
        return x + y

    result = func(1, 2)

    assert result == 3


def test_log_good_file_log(capsys):
    """Тест записи в файл после успешного выполнения"""

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y

    func(1, 2)

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert f"{func.__name__} ok" in logs


def test_log_exception(capsys):
    """Тест вывода после ошибки в консоль"""

    @log()
    def func(x, y):
        return x + y

    func(1, "2")

    captured = capsys.readouterr()

    assert f"{func.__name__} error:" in captured.out


def test_log_exception_file_log(capsys):
    """Тест записb в файл после ошибки"""

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y

    func(1, "2")

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert f"{func.__name__} error" in logs
