from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, '#login')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')


class ContactsPageLocators:
    CREATE_CONTACT = (By.CSS_SELECTOR, '.o-kanban-button-new')
    COMPANY_TYPE_RADIOBUTTON = (By.CSS_SELECTOR, '[data-value="company"]+label')
    COMPANY_NAME_FIELD = (By.CSS_SELECTOR, '[placeholder="Name"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[name="email"]')
    COMPANY_COUNTRY_DROPDOWN = (By.CSS_SELECTOR, '[name="country_id"]  .ui-autocomplete-input')
    SAVE_COMPANY = (By.CSS_SELECTOR, '.o_form_button_save')
    CONTACT_CREATED_MSG = (By.XPATH, '//p[text()="Contact created"]')


class MainPageLocators:
    SALES_APP = (By.CSS_SELECTOR, '[data-menu-xmlid="sale.sale_menu_root"]')
    CRM_APP = (By.CSS_SELECTOR, '[data-menu-xmlid="crm.crm_menu_root"]')
    USER_MENU_BAR = (By.CSS_SELECTOR, '.o_user_menu')
    CONTACTS_APP = (By.CSS_SELECTOR, '[data-menu-xmlid="contacts.menu_contacts"]')


class CRMLocators:
    CREATE_OPP_LIST_VIEW = (By.CSS_SELECTOR, '.o_list_button_add')
    CREATE_CRM_BUTTON = (By.CSS_SELECTOR, '.o-kanban-button-new')
    OPPORTUNITY_NAME_LIST_VIEW = (By.CSS_SELECTOR, '[placeholder="e.g. Product Pricing"]')
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
    USD_CLIENT = (By.XPATH, '//a[text()="Tom Patterson"]')
    EU_CLIENT = (By.XPATH, '//a[text()="IBM Italy"]')


class ProformaLocators:
    ADD_A_PRODUCT_BUTTON = (By.XPATH, '//a[text()="Add a product"]')
    PRODUCT_FIELD = (By.CSS_SELECTOR, '[name="product_id"] .ui-autocomplete-input')
    SELECT_FROM_DROPDOWN = (By.XPATH, '//a[text()="[Solo L (US)] HYPERVSN Solo L (US)"]')
    ADD_A_SECTION_BUTTON = (By.XPATH, '//a[text()="Add a section"]')
    PROFORMA_TAB = (By.XPATH, '//a[text() = "Proforma Lines"]')
    PAYMENT_TERMS = (By.CSS_SELECTOR, '[name="payment_term_id"] .o_input_dropdown')
    PAYMENT_TERMS_INPUT = (By.CSS_SELECTOR, '[name="payment_term_id"] input')
    INVOICE_SMARTBUTTON = (By.CSS_SELECTOR, '[class="btn oe_stat_button"][name="action_view_invoice"]')
    DELIVERY_SMARTBUTTON = (By.CSS_SELECTOR, '[class="btn oe_stat_button"][name="action_view_delivery"]')
    SALE_ORDER_LATEST_CONFIRMED_DELIVERY = (By.XPATH, '//td[text()="Nothing to Invoice"]')
    SALE_ORDER_LATEST_CONFIRMED_INVOICE = (By.XPATH, '//td[text()="Fully Invoiced"]')
    SALE_ORDER_TRANSFERS_SMARTBUTTON = (By.CSS_SELECTOR, '[name="action_view_delivery"]')
    SALE_ORDER_INVOICES_SMARTBUTTON = (By.CSS_SELECTOR, '[name="action_view_invoice"]')


class TransferLocators:
    TRANSFER_VALIDATE = (By.XPATH, '//span[text()="Validate"]')
    APPLY_IMMEDIATE_TRANSFER = (By.XPATH, '//span[text()="Apply"]')
    IMMEDIATE_TRANSFER_WINDOW = (By.XPATH, '//h4[text()="Immediate Transfer?"]')
    RETURN_BUTTON = (By.XPATH, '//button[@class="btn btn-secondary"]/span[text()="Return"]')
    SELECT_TRANSFER_FROM_LIST = (By.CSS_SELECTOR, '.ui-sortable .o_data_cell')


class InvoiceLocators:
    INVOICE_VALIDATE = (By.XPATH, '//span[text()="Validate"]')
    INVOICE_PAID_STATE = (By.XPATH, '//div/button[@aria-current="step"][@data-value="open"]')
    INVOICE_FROM_THE_LIST = (By.CSS_SELECTOR, '.o_data_row .o_data_cell')
