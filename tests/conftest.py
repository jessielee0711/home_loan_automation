import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.cathaybk.com.tw/cathaybk/personal/loan/calculator/mortgage-budget/")
    yield driver
    driver.quit()