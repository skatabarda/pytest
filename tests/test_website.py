import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.set_window_size(1280,720)
    yield browser

def test_open_website(browser):
    browser.get("https://okko.sport/sport")
    browser.implicitly_wait(10)



