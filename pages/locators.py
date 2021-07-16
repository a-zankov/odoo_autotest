from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, '#login')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')


class MainPageLocators:
    SALES_APP = (By.CSS_SELECTOR, '[data-menu-xmlid="sale.sale_menu_root"]')
    CRM_APP = (By.CSS_SELECTOR, '[data-menu-xmlid="crm.crm_menu_root"]')
