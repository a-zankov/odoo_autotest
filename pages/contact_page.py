

from .base_page import BasePage
from .locators import ContactsPageLocators
from src.utilities.genericUtilities import generate_random_company
class ContactPage(BasePage):

    def create_company_card(self):

        company_data = generate_random_company()
        company_name = company_data['name']
        company_email = company_data['email']
        self.browser.find_element(*ContactsPageLocators.CREATE_CONTACT).click()
        self.browser.find_element(*ContactsPageLocators.COMPANY_TYPE_RADIOBUTTON).click()
        company_name_field = self.browser.find_element(*ContactsPageLocators.COMPANY_NAME_FIELD)
        company_name_field.send_keys(company_name)
        company_email_field = self.browser.find_element(*ContactsPageLocators.EMAIL_FIELD)
        company_email_field.send_keys(company_email)







