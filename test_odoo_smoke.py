import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.proforma_page import ProformaPage
from config.config import LoginConfig
from pages.login_page import LoginPage
from pages.main_menu_page import MainMenuPage
from pages.crm_page import CRMPage
from pages.transfer_page import TransferPage
from pages.invoice_page import InvoicePage
from pages.contact_page import ContactPage
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
        page.should_be_reachable_login_page()
        page.login_user(email, password)
        page.should_be_successful_login()

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

    @pytest.mark.sale
    def test_confirm_sale_order(self, browser, environment):
        if environment != 'stage':
            pytest.xfail("Test could be unstable if running not on stage env")
        page = MainMenuPage(browser)
        page.open_crm_page()
        opportunity_name = "USD_case_check_invoice(AUTOTEST)"
        customer_name = "Tom Patterson"
        page = CRMPage(browser)
        page.create_opportunity_usd_list_view(opportunity_name, customer_name)
        page.should_be_delivery_smartbutton()

    @pytest.mark.transfer
    def test_validate_transfer_from_sale_order(self, browser, environment):
        if environment != 'stage':
            pytest.xfail("Test could be unstable if running not on stage env")
        page = MainMenuPage(browser)
        page.open_proforma_page()
        page = ProformaPage(browser)
        page.open_latest_confirmed_sale_order_invoice_delivery()
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
        page.open_latest_confirmed_sale_order_invoice()
        page.open_sale_order_invoice()
        page = InvoicePage(browser)
        WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//li[text()="Invoices"]')))
        page.open_invoice_from_list()
        page.validate_invoice()
        page.should_be_invoice_paid()

    def test_check_taxation_logic(self, browser, environment):
        link = f"https://{environment}-company.kino-mo.com/web#id=3515&action=458&model=sale.order&view_type=form&menu_id=299"
        page = ProformaPage(browser)
        page.open(link)
        time.sleep(3)
        page.check_sale_order_taxes()
        time.sleep(3)

    def test_check_invoice_split_from_one_warehouse(self, browser, environment):
        page = MainMenuPage(browser)
        page.open_crm_page()
        opportunity_name = "Check_invoice_splitting_one_warehouse(AUTOTEST)"
        customer_name = "IBM Italy"
        page = CRMPage(browser)
        page.create_sale_order_one_warehouse(opportunity_name, customer_name)
        page.should_be_delivery_smartbutton()

    @pytest.mark.debuging
    def test_check_invoice_split_from_different_warehouses(self, browser, environment):
        page = MainMenuPage(browser)
        page.open_crm_page()
        opportunity_name = "Check_invoice_splitting_different_warehouses(AUTOTEST)"
        customer_name = "IBM Italy"
        page = CRMPage(browser)
        page.create_sale_order_different_warehouses(opportunity_name, customer_name)
        page.should_be_delivery_smartbutton()
        page = ProformaPage(browser)
        page.open_sale_order_delivery()
        page = TransferPage(browser)
        page.validate_several_transfers()
        WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Invoices"]')))
        page = InvoicePage(browser)
        page.verify_location_vat_several_warehouses(browser)



class TestContactCreation:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request, browser, environment):
        cfg = LoginConfig(user_type='default')
        link = f"https://{environment}-company.kino-mo.com/web/login"
        email = cfg.login
        password = cfg.password
        page = LoginPage(browser)
        page.open(link)
        page.login_user(email, password)

    def test_create_company(self, browser, environment):
        page = MainMenuPage(browser)
        link = f"https://{environment}-company.kino-mo.com/"
        page.open_contacts_page()
        page = ContactPage(browser)
        page.create_company_card()
        page.should_be_company_create()
