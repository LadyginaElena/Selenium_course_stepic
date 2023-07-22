from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pytest

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера


@pytest.fixture()
def browser():
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    browser.implicitly_wait(15)
    yield browser
    browser.quit()


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")
