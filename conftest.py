import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
from pyvirtualdisplay import Display

load_dotenv()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help='Choose browser language')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    display = None
    if not int(os.getenv('SHOW_BROWSER', 0)):
        display = Display(visible=False)
        display.start()
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
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
