from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import InvoiceLocators


class InvoicePage(BasePage):

    def validate_invoice(self):
        self.browser.find_element(*InvoiceLocators.INVOICE_VALIDATE).click()


