from selenium import webdriver
import pytest


@pytest.mark.selenium
def test_python_org():

    browser = webdriver.Chrome()
    browser.get("https://www.python.org")
    assert "Python" in browser.title
