import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/explicit_wait2.html"

try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(5) # Неявное ождиание, чтобы не уронить тест случайно из-за скрипта или инета
    driver.get(link)
    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '100'))
    button = driver.find_element(By.CSS_SELECTOR,'#book')
    button.click()
    x_element = driver.find_element(By.CSS_SELECTOR,'#input_value')
    x = x_element.text
    y = calc(x)
    form = driver.find_element(By.CSS_SELECTOR,'#answer')
    form.send_keys(y)
    button = driver.find_element(By.CSS_SELECTOR,'#solve')
    button.click()




finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    driver.quit()