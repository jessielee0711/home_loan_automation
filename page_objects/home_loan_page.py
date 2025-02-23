from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class HomeLoanPage:
    def __init__(self, driver):
        self.driver = driver
        self.city_dropdown_container = (By.XPATH, "(//div[contains(@class, 'cubinvest-c-selectBox__main')])[1]")
        self.city_dropdown = (By.ID, "cityLtv")
        self.district_dropdown_container = (By.XPATH, "(//div[contains(@class, 'cubinvest-c-selectBox__main')])[2]")
        self.district_dropdown = (By.ID, "areaLtv")
        self.loan_amount_input = (By.ID, "txtAmount")
        self.loan_term_20y = (By.XPATH, "//label[@for='rdoLoanTerm20y']")
        self.loan_term_30y = (By.XPATH, "//label[@for='rdoLoanTerm30y']")
        self.loan_term_other = (By.XPATH, "//label[@for='rdoLoanTermOther']")
        self.loan_term_other_input = (By.ID, "txtLoanTermOtherYear")
        self.loan_rate = (By.ID, "txtInterestRate")
        self.city_error_message = (By.XPATH, "(//div[contains(@class, 'cubinvest-o-formError')])[1]")
        self.district_error_message = (By.XPATH, "(//div[contains(@class, 'cubinvest-o-formError')])[2]")
        self.loan_amount_error_message = (By.XPATH, "(//div[contains(@class, 'cubinvest-o-formError')])[3]")
        self.loan_term_other_error_message = (By.XPATH, "(//div[contains(@class, 'cubinvest-o-formError')])[4]")
        self.loan_rate_error_message = (By.XPATH, "(//div[contains(@class, 'cubinvest-o-formError')])[5]")
        self.start_calculation_button = (By.ID, "btnCalculate")
        self.recalculate_button = (By.ID, "btnReset")
        self.calculation_result_title = (By.XPATH, "//h3[contains(text(), '試算結果')]")

    def select_city(self, city_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.city_dropdown_container)).click()
        city_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.city_dropdown))
        select = Select(city_element)
        select.select_by_visible_text(city_name)

    def select_district(self, district_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.district_dropdown_container)).click()
        district_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.district_dropdown))
        select = Select(district_element)
        select.select_by_visible_text(district_name)

    def enter_loan_amount(self, amount):
        loan_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.loan_amount_input))
        loan_input.clear()
        loan_input.send_keys(amount)

    def select_loan_term(self, term):
        term_mapping = {"20年": self.loan_term_20y, "30年": self.loan_term_30y, "其他": self.loan_term_other}
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(term_mapping[term])).click()

    def enter_loan_rate(self, amount):
        loan_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.loan_rate))
        loan_input.clear()
        loan_input.send_keys(amount)

    def get_error_message(self, error_element):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(error_element)).text
        except:
            return None

    def get_input_value(self, element):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(element)).get_attribute("value")

    def start_calculation(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.start_calculation_button)).click()

    def recalculate(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.recalculate_button)).click()

    def is_calculation_result_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.calculation_result_title)) is not None