# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize("a,b,c",
                         [
                             (1, 2, 3),
                             (2, 3, 5),
                             (1, 1, 4),
                             (0, 1, 1)
                         ])
def test_sum():
    """
    Если сложить 2 и 2,
    получится 4
    """
    assert 2 + 2 == 4
