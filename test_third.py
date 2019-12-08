import pytest


def test_random_lists(create_example_for_test):
    assert create_example_for_test[0] != create_example_for_test[1]
