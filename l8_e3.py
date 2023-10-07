import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 


link = "https://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(link)
    fn = driver.find_element(By.NAME, 'firstname')
    fn.send_keys('ivan')
    ln = driver.find_element(By.NAME, 'lastname')
    ln.send_keys('ivanov')
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('iv@mail.ru')
    file = driver.find_element(By.CSS_SELECTOR, '#file')
    file.send_keys(file_path)
    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    driver.quit()