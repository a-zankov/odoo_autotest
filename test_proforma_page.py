import time

from .pages.login_page import LoginPage
from .pages.main_menu_page import MainMenuPage
from .pages.crm_page import CRMPage
import pytest


class TestProformaDemo:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, environment):
        link = f"https://{environment}-company.kino-mo.com/web/login"
        email = "a.zankov@hypervsn.com"
        password = "e8848c8611"
        page = LoginPage(browser)
        page.open(link)
        page.login_user(email, password)

    @pytest.mark.review
    def test_proforma_flow_usd(self, browser):
        page = MainMenuPage(browser)
        page.open_crm_page()
        opportunity_name = "USD_case(AUTOTEST)"
        customer_name = "Tom Patterson"
        page = CRMPage(browser)
        page.create_opportunity_usd(opportunity_name, customer_name)

    @pytest.mark.correct
    def test_proforma_flow_eur(self, browser):
        page = MainMenuPage(browser)
        page.open_crm_page()
        opportunity_name = "EUR_case(AUTOTEST)"
        customer_name = "Business Consulting Events & Communication S.r.l.s"
        page = CRMPage(browser)
        page.create_opportunity_eur(opportunity_name, customer_name)

    def test_proforma_flow_gbp(self, browser):
        page = MainMenuPage(browser)
        page.open_crm_page()
        opportunity_name = "GBP_case(AUTOTEST)"
        customer_name = "SpaceCraft Industriers"
        page = CRMPage(browser)
        page.create_opportunity_gbp(opportunity_name, customer_name)







