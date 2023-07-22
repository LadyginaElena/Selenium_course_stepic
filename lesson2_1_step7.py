from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("http://suninjuly.github.io/get_attribute.html")
    chest = browser.find_element(By.CSS_SELECTOR, "[src*='.png']")
    x = int(chest.get_attribute("valuex"))

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, '[value="robots"]').click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
