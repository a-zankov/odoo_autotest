import time

from .pages.login_page import LoginPage
from .pages.main_menu_page import MainMenuPage
from .pages.crm_page import CRMPage
import pytest


class TestClickApps:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://dev-company.kino-mo.com/web/login"
        email = "a.zankov@hypervsn.com"
        password = "e8848c8611"
        page = LoginPage(browser, link)
        page.open()
        page.login_user(email, password)

    def test_click_all_apps(self, browser):
        link = "https://dev-company.kino-mo.com/web?"
        page = MainMenuPage(browser, link)
        page.click_all_apps()
