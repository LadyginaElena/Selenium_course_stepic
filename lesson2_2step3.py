from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("http://suninjuly.github.io/selects2.html")
    num1 = browser.find_element(By.ID, "num1")
    num1 = num1.text
    num2 = browser.find_element(By.ID, "num2")
    num2 = num2.text

    sum = int(num1) + int(num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_value(str(sum))
    select.select_by_visible_text(str(sum))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
