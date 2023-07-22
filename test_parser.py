from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
import pytest

link = "http://selenium1py.pythonanywhere.com/"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        service = Service(executable_path=ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
        browser.implicitly_wait(15)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        service = Service(executable_path=GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service)
        browser.implicitly_wait(15)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
# pytest -s -v --browser_name=chrome selenium_course_stepic/test_parser.py
# pytest -s -v --browser_name=firefox selenium_course_stepic/test_parser.py
