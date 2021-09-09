import time
from selenium.webdriver.common.by import By

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
        company_country = self.browser.find_element(*ContactsPageLocators.COMPANY_COUNTRY_DROPDOWN)
        company_country.send_keys("Poland")
        self.browser.find_element(By.XPATH, '//a[text()="Poland"]').click()
        self.browser.find_element(*ContactsPageLocators.SAVE_COMPANY).click()
        time.sleep(5)

    def should_be_company_create(self):
        assert self.is_element_present(*ContactsPageLocators.CONTACT_CREATED_MSG), "Company card has not been created" \
                                                                                   "successfully"



