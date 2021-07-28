from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, '#login')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')


class MainPageLocators:
    SALES_APP = (By.CSS_SELECTOR, '[data-menu-xmlid="sale.sale_menu_root"]')
    CRM_APP = (By.CSS_SELECTOR, '[data-menu-xmlid="crm.crm_menu_root"]')


class CRMLocators:
    CREATE_CRM_BUTTON = (By.CSS_SELECTOR, '.o-kanban-button-new')
    OPPORTUNITY_NAME = (By.CSS_SELECTOR, '.o_field_char')
    CUSTOMER_NAME = (By.CSS_SELECTOR, '.ui-autocomplete-input')
    OPPORTUNITY_ADD_TO_KANBAN = (By.CSS_SELECTOR, '.o_kanban_add')
    OPPORTUNITY_EDIT_KANBAN_VIEW = (By.CSS_SELECTOR, '.o_kanban_edit')
    SELECT_FROM_DROPDOWN = (By.CSS_SELECTOR, '.ui-menu-item>a')
    SAVE_OPPORTUNITY_CARD = (By.CSS_SELECTOR, '.o_form_button_save')
    DEAL_TYPE = (By.CSS_SELECTOR, '[name="deal_type"] .ui-autocomplete-input')
    DEAL_TYPE_SELECT = (By.XPATH, '//a[text()="POC"]')
    REFERRED_BY = (By.CSS_SELECTOR, '[name="referred_by"] .ui-autocomplete-input')
    TYPE_OF_CONVERSATION = (By.XPATH, '//label[text()="Type of Conversion"]')
    REFERRED_BY_SELECT = (By.XPATH, '//a[text()="FB Leads Center"]')
    EXPECTED_CLOSING = (By.CSS_SELECTOR, '.o_datepicker_input[name="date_deadline"]')
    CREATE_PROFORMA_FROM_OPP = (By.CSS_SELECTOR, '[name="action_create_new_sale_order"]')

class ProformaLocators:
    ADD_A_PRODUCT_BUTTON = (By.XPATH, '//a[text()="Add a product"]')
    PRODUCT_FIELD = (By.CSS_SELECTOR, '[name="product_id"] .ui-autocomplete-input')
    SELECT_FROM_DROPDOWN = (By.XPATH, '//a[text()="[Solo L (US)] HYPERVSN Solo L (US)"]')
    ADD_A_SECTION_BUTTON = (By.XPATH, '//a[text()="Add a section"]')
    PROFORMA_TAB = (By.XPATH, '//a[text() = "Proforma Lines"]')



