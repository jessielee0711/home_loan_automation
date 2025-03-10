import pytest


@pytest.mark.parametrize("city, district", [
    ("基隆市", "不分區"),
    ("台北市", "信義區"),
    ("新北市", "板橋區"),
    ("桃園縣", "中壢市"),
    ("台中市", "南屯區"),
    ("台南市", "中西區"),
    ("高雄市", "三民區")
])
def test_select_city_district(home_loan_page, city, district):
    home_loan_page.select_city(city)
    home_loan_page.select_district(district)
    assert home_loan_page.get_error_message(home_loan_page.city_error_message) is None
    assert home_loan_page.get_error_message(home_loan_page.district_error_message) is None


def test_error_messages(home_loan_page):
    home_loan_page.start_calculation()
    assert home_loan_page.get_error_message(home_loan_page.city_error_message) == "請選擇縣市"
    assert home_loan_page.get_error_message(home_loan_page.district_error_message) == "請選擇行政區"
    assert home_loan_page.get_error_message(home_loan_page.loan_amount_error_message) == "請輸入整數貸款金額"
    assert home_loan_page.get_error_message(home_loan_page.loan_term_other_error_message) == "請輸入貸款年限"
    assert home_loan_page.get_error_message(home_loan_page.loan_rate_error_message) == "請輸入數字"


def test_valid_loan_amount(home_loan_page):
    home_loan_page.enter_loan_amount("1000000")
    assert home_loan_page.get_error_message(home_loan_page.loan_amount_error_message) is None


def test_invalid_loan_amount(home_loan_page):
    home_loan_page.enter_loan_amount("abc")
    home_loan_page.start_calculation()
    assert home_loan_page.get_error_message(home_loan_page.loan_amount_error_message) == "請輸入整數貸款金額"


def test_loan_term_selection(home_loan_page):
    for term in ["20年", "30年", "其他"]:
        home_loan_page.select_loan_term(term)


def test_calculation_results_displayed(home_loan_page):
    home_loan_page.select_city("台北市")
    home_loan_page.select_district("信義區")
    home_loan_page.enter_loan_amount("1000000")
    home_loan_page.select_loan_term("20年")
    home_loan_page.enter_loan_rate("3")
    home_loan_page.start_calculation()
    assert home_loan_page.is_calculation_result_displayed()


def test_recalculate(home_loan_page):
    home_loan_page.select_city("台北市")
    home_loan_page.select_district("信義區")
    home_loan_page.enter_loan_amount("1000000")
    home_loan_page.select_loan_term("20年")
    home_loan_page.start_calculation()
    home_loan_page.recalculate()

    assert home_loan_page.get_input_value(home_loan_page.city_dropdown) == ""
    assert home_loan_page.get_input_value(home_loan_page.district_dropdown) == ""
    assert home_loan_page.get_input_value(home_loan_page.loan_amount_input) == ""
    assert home_loan_page.get_input_value(home_loan_page.loan_rate) == ""