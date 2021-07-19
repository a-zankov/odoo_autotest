import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import ProformaLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def add_a_product_to_proforma(self, product_name, qty=1, proforma_level=False):
        self.browser.find_element(*ProformaLocators.ADD_A_PRODUCT_BUTTON).click()
        time.sleep(1)
        self.browser.find_element(*ProformaLocators.PRODUCT_FIELD).send_keys(product_name)
        self.browser.find_element(By.XPATH, f'//a[text()="{product_name}"]').click()
        if qty > 1:
            self.browser.find_element(By.CSS_SELECTOR, '[name="product_uom_qty"]').clear()
            self.browser.find_element(By.CSS_SELECTOR, '[name="product_uom_qty"]').send_keys(qty)
        if proforma_level:
            self.browser.find_element(By.CSS_SELECTOR, '[name="level_id"] .o_input').click()
            self.browser.find_element(By.XPATH, '//a[text()="End-User"]').click()
        self.browser.find_element(*ProformaLocators.PROFORMA_TAB).click()
        time.sleep(1)

    def add_a_section_to_proforma(self, section_name):
        add_button = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Add a section"]')))
        add_button.click()
        self.browser.find_element(By.CSS_SELECTOR, '.o_selected_row .o_data_cell>.o_input').send_keys(section_name)
        self.browser.find_element(*ProformaLocators.PROFORMA_TAB).click()
        time.sleep(1)




