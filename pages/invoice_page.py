import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import InvoiceLocators
from .locators import ProformaLocators


class InvoicePage(BasePage):

    def validate_invoice(self):
        self.browser.find_element(*InvoiceLocators.INVOICE_VALIDATE).click()

    def verify_location_vat_several_warehouses(self, browser):
        unit_price_elem = self.browser.find_element(By.CSS_SELECTOR, '[name="price_unit"]')
        unit_price = unit_price_elem.text
        self.browser.find_element(*ProformaLocators.SALE_ORDER_INVOICES_SMARTBUTTON).click()
        WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//li[text()="Invoices"]')))
        self.browser.find_element(By.XPATH, f'//td[contains(text(), {unit_price})]').click()
        self.open_other_info_tab()
        self.should_be_correct_location_vat("LT100013874019")
        self.select_next_object_kanban_view()
        time.sleep(3)
        self.should_be_correct_location_vat("IE3564381RH")

    def open_invoice_from_list(self):
        self.browser.find_element(*InvoiceLocators.INVOICE_FROM_THE_LIST).click()

    def should_be_invoice_paid(self):
        assert self.is_element_present(*InvoiceLocators.INVOICE_PAID_STATE), "Invoice is not paid"

    def should_be_correct_location_vat(self, location_vat):
        location_vat_value_elem = self.browser.find_element(By.CSS_SELECTOR, '[name="location_company_vat"]')
        location_vat_value = location_vat_value_elem.text
        assert location_vat == location_vat_value, "Location company VAT didn't match expected value.\n" \
                                                   f"Expected: {location_vat}. Actual: {location_vat_value}"
