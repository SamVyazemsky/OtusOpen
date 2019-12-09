import pytest


def test_sum():
    """
    Если сложить 2 и 2,
    получится 4
    """
    assert 2 + 2 == 4


def test_divizion():
    """
    1. Разделить 4 на 2
    2. Сравнить ответ с 2
    """
    assert 4 / 2 == 2


def test_divizion_by_zero():
    """
    При делении на 0
    вызывается ошибка ZeroDivisionError
    """
    with pytest.raises(ZeroDivisionError):
        print(4 / 0)

