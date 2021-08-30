from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def login_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        pass_field.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def should_be_reachable_login_page(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Webdriver didn't reach Login Page"

    def should_be_successful_login(self):
        assert self.is_element_present(*MainPageLocators.USER_MENU_BAR), "Can't login, verify user's credentials"
