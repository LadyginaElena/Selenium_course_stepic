from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import math
import time

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# driver.get("https://stepik.org/lesson/25969/step/8")
# "https://stepik.org/lesson/236898/step/1"

numbers = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]


@pytest.fixture()
def browser():
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    browser.implicitly_wait(15)
    yield browser
    browser.quit()


@pytest.mark.parametrize("endpoint", numbers)
class TestParametrize:
    def test_user_should_be_authorization(self, browser, endpoint):
        link = f"https://stepik.org/lesson/{endpoint}/step/1"
        browser.get(link)
        enter = browser.find_element(By.ID, "ember33")
        enter.click()
        browser.switch_to.active_element
        user_name = browser.find_element(
            By.ID,
            "id_login_email",
        )
        user_name.clear()
        user_name.send_keys("ladygina.ev@mail.ru")
        password = browser.find_element(By.ID, "id_login_password")
        password.clear()
        password.send_keys("Orda352")
        button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
        button.click()
        WebDriverWait(browser, 15).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "navbar__profile-img"))
        )
        answer = math.log(int(time.time()))
        input_field = browser.find_element(By.TAG_NAME, "textarea")
        input_field.send_keys(str(answer))
        (
            WebDriverWait(browser, 15).until(
                ec.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
            )
        ).click()
        WebDriverWait(browser, 10).until(
            ec.text_to_be_present_in_element(
                (By.CLASS_NAME, "again-btn white"), "Решить снова"
            )
        )
        get_txt = WebDriverWait(browser, 15).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
        text = get_txt.text
        assert text == "Correct!", f"text={text}"
