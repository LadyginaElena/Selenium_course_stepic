from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random
import string
import os

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("http://suninjuly.github.io/file_input.html")
    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    letters = string.ascii_lowercase
    random_word = "".join(random.choice(letters) for _ in range(8))
    for element in [first_name, last_name, email]:
        element.send_keys(random_word)

    current_dir = os.path.abspath(
        os.path.dirname(__file__)
    )  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(
        current_dir, "file.txt"
    )  # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, 'input[name="file"]')
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
