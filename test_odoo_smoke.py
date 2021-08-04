import time

from .config.config import LoginConfig
from .pages.login_page import LoginPage
from .pages.main_menu_page import MainMenuPage
from .pages.crm_page import CRMPage
import pytest


class TestClickApps:
    @pytest.fixture(scope="function", autouse=True, params=['default', 'helpdesk', 'financial', 'sales'])
    def setup(self, request, browser):
        cfg = LoginConfig(user_type=request.param)
        link = "https://stage-company.kino-mo.com/web/login"
        email = cfg.login
        password = cfg.password
        page = LoginPage(browser)
        page.open(link)
        page.login_user(email, password)

    def test_click_all_apps(self, browser):
        page = MainMenuPage(browser)
        page.click_all_apps()
