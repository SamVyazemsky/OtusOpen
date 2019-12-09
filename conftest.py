import pytest
import selenium
import random


@pytest.fixture()
def create_example_for_test():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    return a, b

'''
@pytest.fixture()
def setup_teardown_test():
    print("setup")
    yield
    print("teardown")
'''