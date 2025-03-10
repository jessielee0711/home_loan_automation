import pytest
from selenium import webdriver
from page_objects.home_loan_page import HomeLoanPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.cathaybk.com.tw/cathaybk/personal/loan/calculator/mortgage-budget/")
    yield driver
    driver.quit()

@pytest.fixture
def home_loan_page(driver):
    return HomeLoanPage(driver)