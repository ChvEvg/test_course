import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(link)
    x_element = driver.find_element(By.CSS_SELECTOR, '.form-group span:nth-child(2)')
    x = x_element.text
    y = calc(x)
    form = driver.find_element(By.CSS_SELECTOR, '#answer')
    form.send_keys(y)
    checkbox = driver.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()
    radio = driver.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio.click()
    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    driver.quit()