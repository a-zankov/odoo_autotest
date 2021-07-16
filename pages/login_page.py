from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def login_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        pass_field.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()



