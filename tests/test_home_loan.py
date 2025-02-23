import pytest
from page_objects.home_loan_page import HomeLoanPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("city, district", [
    ("基隆市", "不分區"),
    ("台北市", "信義區"),
    ("新北市", "板橋區"),
    ("桃園縣", "中壢市"),
    ("台中市", "南屯區"),
    ("台南市", "中西區"),
    ("高雄市", "三民區")
])

def test_select_city_district(driver, city, district):
    page = HomeLoanPage(driver)
    page.select_city(city)
    page.select_district(district)
    assert page.get_error_message(page.city_error_message) is None
    assert page.get_error_message(page.district_error_message) is None

def test_error_messages(driver):
    page = HomeLoanPage(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.loan_term_other)).click()
    page.start_calculation()
    assert page.get_error_message(page.city_error_message) == "請選擇縣市"
    assert page.get_error_message(page.district_error_message) == "請選擇行政區"
    assert page.get_error_message(page.loan_amount_error_message) == "請輸入整數貸款金額"
    assert page.get_error_message(page.loan_term_other_error_message) == "請輸入貸款年限"
    assert page.get_error_message(page.loan_rate_error_message) == "請輸入數字"

def test_valid_loan_amount(driver):
    page = HomeLoanPage(driver)
    page.enter_loan_amount("1000000")
    assert page.get_error_message(page.loan_amount_error_message) is None

def test_invalid_loan_amount(driver):
    page = HomeLoanPage(driver)
    page.enter_loan_amount("abc")
    page.start_calculation()
    assert page.get_error_message(page.loan_amount_error_message) == "請輸入整數貸款金額"

def test_loan_term_selection(driver):
    page = HomeLoanPage(driver)
    for term in ["20年", "30年", "其他"]:
        page.select_loan_term(term)

def test_calculation_results_displayed(driver):
    page = HomeLoanPage(driver)
    page.select_city("台北市")
    page.select_district("信義區")
    page.enter_loan_amount("1000000")
    page.select_loan_term("20年")
    page.enter_loan_rate("3")
    page.start_calculation()
    assert page.is_calculation_result_displayed()

def test_recalculate(driver):
    page = HomeLoanPage(driver)
    page.select_city("台北市")
    page.select_district("信義區")
    page.enter_loan_amount("1000000")
    page.select_loan_term("20年")
    page.start_calculation()
    page.recalculate()

    assert page.get_input_value(page.city_dropdown) == ""
    assert page.get_input_value(page.district_dropdown) == ""
    assert page.get_input_value(page.loan_amount_input) == ""
    assert page.get_input_value(page.loan_rate) == ""