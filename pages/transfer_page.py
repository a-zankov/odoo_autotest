from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import TransferLocators


class TransferPage(BasePage):

    def validate_transfer(self):
        self.browser.find_element(*TransferLocators.TRANSFER_VALIDATE).click()
        immediate_transfer = self.browser.find_element(*TransferLocators.IMMEDIATE_TRANSFER_WINDOW)
        if immediate_transfer:
            self.browser.find_element(*TransferLocators.APPLY_IMMEDIATE_TRANSFER).click()
        WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Return"]')))

    def should_be_transfer_validated(self):
        assert self.is_element_present(*TransferLocators.RETURN_BUTTON), \
            "Transfer has not been validated"
