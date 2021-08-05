import time

from .config.config import LoginConfig
from .pages.login_page import LoginPage
from .pages.main_menu_page import MainMenuPage
from .pages.crm_page import CRMPage
import pytest


class TestClickApps:
    #@pytest.fixture(scope="function", autouse=True, params=['default', 'helpdesk', 'financial', 'sales'])
    @pytest.fixture(scope="function", autouse=True, params=['default'])
    def setup(self, request, browser, environment):
        cfg = LoginConfig(user_type=request.param)
        link = f"https://{environment}-company.kino-mo.com/web/login"
        email = cfg.login
        password = cfg.password
        page = LoginPage(browser)
        page.open(link)
        page.login_user(email, password)

    def test_click_all_apps(self, browser, environment):
        page = MainMenuPage(browser)
        link = f"https://{environment}-company.kino-mo.com/"
        page.click_all_apps(link)
