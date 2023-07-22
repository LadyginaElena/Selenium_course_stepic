import time
import math
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pytest

numbers = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]


@pytest.fixture()
def browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
        prompt = browser.switch_to.active_element
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
        input_field = WebDriverWait(browser, 15).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, ".textarea"))
        )
        time.sleep(3)
        input_field.clear()
        input_field.send_keys(str(answer))
        (
            WebDriverWait(browser, 15).until(
                ec.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
            )
        ).click()
        # button2 = browser.find_element((By.CLASS_NAME, "submit-submission")).click()
        get_txt = WebDriverWait(browser, 15).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
        text = get_txt.text
        time.sleep(3)
        print(text)
        assert text == "Correct!", f"text={text}"
        print(text)
