import pytest

from src.decorators import my_function


def test_log():
    with pytest.raises(TypeError):
        my_function("1", 2)
    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)


def test_console_output(capsys):
    result = my_function(3, 1)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
