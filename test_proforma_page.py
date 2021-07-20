import time

from .pages.login_page import LoginPage
from .pages.main_menu_page import MainMenuPage
from .pages.crm_page import CRMPage
import pytest


class TestProformaDemo:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://dev-company.kino-mo.com/web/login"
        email = "a.zankov@hypervsn.com"
        password = "e8848c8611"
        page = LoginPage(browser, link)
        page.open()
        page.login_user(email, password)

    @pytest.mark.correct
    def test_proforma_flow_usd(self, browser):
        link = "https://dev-company.kino-mo.com/web?"
        page = MainMenuPage(browser, link)
        page.open_crm_page()
        opportunity_name = "USD_case(AUTOTEST)"
        customer_name = "Tom Patterson"
        page = CRMPage(browser, link)
        page.create_opportunity_usd(opportunity_name, customer_name)

    @pytest.mark.review
    def test_proforma_flow_eur(self, browser):
        link = "https://dev-company.kino-mo.com/web?"
        page = MainMenuPage(browser, link)
        page.open_crm_page()
        opportunity_name = "EUR_case(AUTOTEST)"
        customer_name = "Business Consulting Events & Communication S.r.l.s"
        page = CRMPage(browser, link)
        page.create_opportunity_eur(opportunity_name, customer_name)







