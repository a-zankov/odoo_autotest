from .base_page import BasePage
from .locators import MainPageLocators


class MainMenuPage(BasePage):
    def open_crm_page(self):
        crm_app_button = self.browser.find_element(*MainPageLocators.CRM_APP)
        crm_app_button.click()

