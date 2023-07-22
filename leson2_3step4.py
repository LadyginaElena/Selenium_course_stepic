from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("http://suninjuly.github.io/alert_accept.html")
    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.click()
    alert = browser.switch_to.alert
    alert.accept()
    value_text = browser.find_element(By.ID, "input_value")
    text_x = value_text.text

    def calc(text_x):
        return str(math.log(abs(12 * math.sin(int(text_x)))))

    y = calc(text_x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
