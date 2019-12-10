# -*- coding: utf-8 -*-
import pytest


@pytest.mark.calc
@pytest.mark.parametrize("a,b,c",
                         [
                             (1, 2, 3),
                             (2, 3, 5),
                             (1, 1, 4),
                             (0, 1, 1)
                         ])
def test_sum(a, b, c):
    """
    Если сложить 2 и 2,
    получится 4
    """
    if a == 1 and b == 1 and c == 4:
        pytest.xfail('it is error')
    assert a + b == c
