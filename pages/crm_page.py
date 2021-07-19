import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from .locators import CRMLocators
from .locators import ProformaLocators


class CRMPage(BasePage):

    def create_opportunity_usd(self, opportunity_name, customer_name):
        create_opp_button = self.browser.find_element(*CRMLocators.CREATE_CRM_BUTTON)
        create_opp_button.click()
        opp_name = self.browser.find_element(*CRMLocators.OPPORTUNITY_NAME)
        opp_name.send_keys(opportunity_name)
        customer_field = self.browser.find_element(*CRMLocators.CUSTOMER_NAME)
        customer_field.send_keys(customer_name)
        time.sleep(2)
        select_customer = self.browser.find_element(*CRMLocators.SELECT_FROM_DROPDOWN)
        select_customer.click()
        self.browser.find_element(*CRMLocators.OPPORTUNITY_EDIT_KANBAN_VIEW).click()
        time.sleep(2)
        self.browser.find_element(*CRMLocators.DEAL_TYPE).click()
        self.browser.find_element(*CRMLocators.DEAL_TYPE_SELECT).click()
        time.sleep(1)
        self.browser.find_element(*CRMLocators.REFERRED_BY).click()
        self.browser.find_element(*CRMLocators.REFERRED_BY_SELECT).click()
        time.sleep(1)
        self.browser.find_element(*CRMLocators.EXPECTED_CLOSING).send_keys("30 Aug 2021")
        self.browser.find_element(*CRMLocators.CREATE_PROFORMA_FROM_OPP).click()
        time.sleep(3)
        self.add_a_product_to_proforma("[Solo L (US)] HYPERVSN Solo L (US)", 1, True)
        self.add_a_section_to_proforma("Accessories")
        self.add_a_product_to_proforma("[KM-A-DOME-L-100.A] HYPERVSN Dome L", 1, )
        self.add_a_product_to_proforma("[KM-A-TR-100.A] HYPERVSN Tripod", 1, )
        self.add_a_section_to_proforma("Delivery")
        self.add_a_product_to_proforma("[Delivery-E] Accessories delivery (Economy)", 1)
        self.browser.find_element(By.CSS_SELECTOR, '.o_form_button_save').click()
        time.sleep(15)
        self.browser.find_element(By.CSS_SELECTOR, '[name="button_send_to_operation"]').click()
        time.sleep(6)
        self.browser.find_element(By.CSS_SELECTOR, '.fa-close').click()
        self.browser.find_element(By.CSS_SELECTOR, '[id="operation_reviewer_action_confirm"]').click()
        time.sleep(7)


    def create_opportunity_eur(self, opportunity_name, customer_name):
        create_opp_button = self.browser.find_element(*CRMLocators.CREATE_CRM_BUTTON)
        create_opp_button.click()
        opp_name = self.browser.find_element(*CRMLocators.OPPORTUNITY_NAME)
        opp_name.send_keys(opportunity_name)
        customer_field = self.browser.find_element(*CRMLocators.CUSTOMER_NAME)
        customer_field.send_keys(customer_name)
        time.sleep(2)
        select_customer = self.browser.find_element(*CRMLocators.SELECT_FROM_DROPDOWN)
        select_customer.click()
        self.browser.find_element(*CRMLocators.OPPORTUNITY_EDIT_KANBAN_VIEW).click()
        time.sleep(2)
        self.browser.find_element(*CRMLocators.DEAL_TYPE).click()
        self.browser.find_element(*CRMLocators.DEAL_TYPE_SELECT).click()
        time.sleep(1)
        self.browser.find_element(*CRMLocators.REFERRED_BY).click()
        self.browser.find_element(*CRMLocators.REFERRED_BY_SELECT).click()
        time.sleep(1)
        self.browser.find_element(*CRMLocators.EXPECTED_CLOSING).send_keys("30 Aug 2021")
        self.browser.find_element(*CRMLocators.CREATE_PROFORMA_FROM_OPP).click()
        time.sleep(3)
        self.add_a_product_to_proforma("[Solo L (US)] HYPERVSN Solo L (US)", 1, True)
        self.add_a_section_to_proforma("Accessories")
        self.add_a_product_to_proforma("[KM-A-DOME-L-100.A] HYPERVSN Dome L", 1, )
        self.add_a_product_to_proforma("[KM-A-TR-100.A] HYPERVSN Tripod", 1, )
        self.add_a_section_to_proforma("Delivery")
        self.add_a_product_to_proforma("[Delivery-E] Accessories delivery (Economy)", 1)
        self.browser.find_element(By.CSS_SELECTOR, '.o_form_button_save').click()
        time.sleep(15)
        self.browser.find_element(By.CSS_SELECTOR, '[name="button_send_to_operation"]').click()
        time.sleep(6)
        self.browser.find_element(By.CSS_SELECTOR, '.fa-close').click()
        self.browser.find_element(By.CSS_SELECTOR, '[id="operation_reviewer_action_confirm"]').click()
        time.sleep(7)
