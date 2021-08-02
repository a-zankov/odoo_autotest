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

    def click_all_apps(self):
        apps = self.browser.find_elements(By.CSS_SELECTOR, '[class="o_app o_menuitem"]')
        apps_name = []
        for i in apps:
            apps_attr = i.get_attribute("data-menu-xmlid")
            apps_name.append(apps_attr)
        print(apps_name)
        for i in apps_name:
            self.browser.find_element(By.CSS_SELECTOR, f'[data-menu-xmlid="{i}"]').click()
            time.sleep(2)
            back_to_main = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.o_menu_toggle ')))
            back_to_main.click()
            time.sleep(2)
