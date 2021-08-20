
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProformaLocators


class ProformaPage(BasePage):

    def open_latest_confirmed_sale_order(self):
        self.browser.find_element(*ProformaLocators.SALE_ORDER_LATEST_CONFIRMED).click()

    def open_sale_order_delivery(self):
        self.browser.find_element(*ProformaLocators.SALE_ORDER_TRANSFERS_SMARTBUTTON).click()

    def open_sale_order_invoice(self):
        self.browser.find_element(*ProformaLocators.SALE_ORDER_INVOICES_SMARTBUTTON)