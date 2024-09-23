import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser

def test_open_website(browser):
    browser.get("https://alfabank.ru/")
    alfa_cards = browser.find_element(By.XPATH, '//a[text()= "Карты"]')
    alfa_cards.click()
    title = browser.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'Банковские карты'
