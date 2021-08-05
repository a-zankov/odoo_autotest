import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import MainPageLocators


class MainMenuPage(BasePage):
    def open_crm_page(self):
        crm_app_button = self.browser.find_element(*MainPageLocators.CRM_APP)
        crm_app_button.click()

    def click_all_apps(self, link):
        apps = self.browser.find_elements(By.CSS_SELECTOR, '[class="o_app o_menuitem"]')
        print(self.browser.current_url)
        apps_name = []
        for i in apps:
            apps_attr = i.get_attribute("data-menu-xmlid")
            apps_name.append(apps_attr)
        print(apps_name)
        for i in apps_name:
            self.browser.find_element(By.CSS_SELECTOR, f'[data-menu-xmlid="{i}"]').click()
            WebDriverWait(self.browser, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.o_menu_brand')))
            assert "action" in self.browser.current_url or \
                   link == self.browser.current_url, f"Can't open menu '{i}'"
            while True:
                back_to_main = WebDriverWait(self.browser, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.o_menu_toggle')))
                back_to_main.click()
                app_elem = WebDriverWait(self.browser, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="o_app o_menuitem"]')))
                if app_elem:
                    break

