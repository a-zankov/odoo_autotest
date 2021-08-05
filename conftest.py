import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
from pyvirtualdisplay import Display

# load_dotenv()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help='Choose browser language')
    parser.addoption('--virtual_display', action='store', default='on',
                     help='Choose virtual_display mode: on or off')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    virtual_display = request.config.getoption("virtual_display")
    if virtual_display == "on":
        display = Display(visible=True, size=(1920, 1080), backend="xvfb")
        display.start()
        print("\nvirtual display starts...")
    elif virtual_display == "off":
        display = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-dev-shm-using")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        # options.add_argument('headless')
        options.add_experimental_option('excludeSwitches',
                                        ['enable-logging'])  # выбрасываем мусор из логов (опция для Windows)
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
    if display:
        display.stop()
        print("\nvirtual display closed...")
