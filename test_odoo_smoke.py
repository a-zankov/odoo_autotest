import time

from .pages.proforma_page import ProformaPage
from .config.config import LoginConfig
from .pages.login_page import LoginPage
from .pages.main_menu_page import MainMenuPage
from .pages.crm_page import CRMPage
from .pages.transfer_page import TransferPage
from .pages.invoice_page import InvoicePage
import pytest


class TestClickApps:
    @pytest.fixture(scope="function", autouse=True, params=['default', 'helpdesk', 'financial', 'sales'])
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


class TestSalePipeline:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request, browser, environment):
        cfg = LoginConfig(user_type='default')
        link = f"https://{environment}-company.kino-mo.com/web/login"
        email = cfg.login
        password = cfg.password
        page = LoginPage(browser)
        page.open(link)
        page.login_user(email, password)

    @pytest.mark.debuging
    def test_confirm_sale_order(self, browser, environment):
        if environment != 'stage':
            pytest.xfail("Test could be unstable if running not on stage env")
        page = MainMenuPage(browser)
        page.open_crm_page()
        opportunity_name = "USD_case_check_invoice(AUTOTEST)"
        customer_name = "Tom Patterson"
        page = CRMPage(browser)
        page.create_opportunity_usd_list_view(opportunity_name, customer_name)
        page.should_be_invoice_smartbutton()

    @pytest.mark.debuging
    def test_validate_transfer_from_sale_order(self, browser, environment):
        if environment != 'stage':
            pytest.xfail("Test could be unstable if running not on stage env")
        page = MainMenuPage(browser)
        page.open_proforma_page()
        page = ProformaPage(browser)
        page.open_latest_confirmed_sale_order()
        page.open_sale_order_delivery()
        page = TransferPage(browser)
        page.validate_transfer()
        page.should_be_transfer_validated()

    def test_validate_invoice_from_sale_order(self, browser, environment):
        if environment != 'stage':
            pytest.xfail("Test could be unstable if running not on stage env")
        page = MainMenuPage(browser)
        page.open_proforma_page()
        page = ProformaPage(browser)
        page.open_latest_confirmed_sale_order()
        page.open_sale_order_invoice()
        page = InvoicePage(browser)







