import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(2)
    yield browser
    browser.close()