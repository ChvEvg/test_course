import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://suninjuly.github.io/registration2.html"

try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(link)
    # Код для заполнения формы
    f_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
    f_name.send_keys('IVAN')
    l_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
    l_name.send_keys('IVANOV')
    email = driver.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
    email.send_keys('ivivanov@mail.ru')
    # phone = driver.find_element(By.CSS_SELECTOR, '.second_block .first_class input')
    # phone.send_keys('+79999999999')
    # address = driver.find_element(By.CSS_SELECTOR, '.second_block .second_class input')
    # address.send_keys('net adresa')

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text



finally:
    # закрываем браузер после всех манипуляций
    time.sleep(8)
    driver.quit()