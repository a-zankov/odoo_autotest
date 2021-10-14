import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProformaLocators


class ProformaPage(BasePage):
    def open_latest_confirmed_sale_order_invoice_delivery(self):
        self.browser.find_element(*ProformaLocators.SALE_ORDER_LATEST_CONFIRMED_DELIVERY).click()

    def open_latest_confirmed_sale_order_invoice(self):
        self.browser.find_element(*ProformaLocators.SALE_ORDER_LATEST_CONFIRMED_INVOICE).click()

    def open_sale_order_delivery(self):
        self.browser.find_element(*ProformaLocators.SALE_ORDER_TRANSFERS_SMARTBUTTON).click()

    def open_sale_order_invoice(self):
        self.browser.find_element(*ProformaLocators.SALE_ORDER_INVOICES_SMARTBUTTON).click()

    def check_sale_order_taxes(self):
        taxes_tags = self.browser.find_elements(By.CSS_SELECTOR, '.o_badge_text')
        taxes_value = [i.get_attribute("title") for i in taxes_tags]
        print(taxes_value)
        uk_invalid_vat_er = ['VAT 20% UK', 'VAT 20% UK', 'VAT 20% UK', 'VAT 20% UK',
                             'VAT 20% UK', 'VAT 20% UK', 'VAT 20% UK', 'VAT 20% UK']
        eu_invalid_vat_er = ['VAT 23% IR', 'VAT 20% UK', 'VAT 20% UK', 'VAT 21% LT',
                             'VAT 21% LT', 'VAT 21% LT', 'VAT 21% LT', 'VAT 20% UK']
        lt_valid_vat_er = []
        ru_vat_er = []


