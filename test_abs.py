from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import random
import string
import pytest


class TestAbs:
    def test_1(self):
        try:
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            browser.get("http://suninjuly.github.io/registration1.html")
            first_name = browser.find_element(
                By.XPATH,
                "//label[contains(text(),'First name*')]/following-sibling::input",
            )
            last_name = browser.find_element(
                By.XPATH,
                "//label[contains(text(),'Last name*')]/following-sibling::input",
            )
            email = browser.find_element(
                By.XPATH, "//label[contains(text(),'Email*')]/following-sibling::input"
            )
            letters = string.ascii_lowercase
            random_word = "".join(random.choice(letters) for _ in range(8))
            for element in [first_name, last_name, email]:
                element.send_keys(random_word)

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(3)
            link_t = browser.find_element(By.TAG_NAME, "h1").text
            assert (
                link_t == "Congratulations! You have successfully registered!"
            ), "registration is failed"
        finally:
            # успеваем скопировать код за 30 секунд
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_2(self):
        try:
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            browser.get("http://suninjuly.github.io/registration2.html")
            first_name = browser.find_element(
                By.XPATH,
                "//label[contains(text(),'First name*')]/following-sibling::input",
            )

            with pytest.raises(NoSuchElementException):
                browser.find_element(
                    By.XPATH,
                    "//label[contains(text(),'Last name*')]/following-sibling::input",
                )
                pytest.fail("Не должно быть поля last_name")

            email = browser.find_element(
                By.XPATH, "//label[contains(text(),'Email*')]/following-sibling::input"
            )
            letters = string.ascii_lowercase
            random_word = "".join(random.choice(letters) for _ in range(8))
            for element in [first_name, email]:
                element.send_keys(random_word)

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(3)
            link_t = browser.find_element(By.TAG_NAME, "h1").text
            assert (
                link_t == "Congratulations! You have successfully registered!"
            ), "registration is failed"

        finally:
            # успеваем скопировать код за 30 секунд
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()
