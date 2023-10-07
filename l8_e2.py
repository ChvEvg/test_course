import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"

try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(link)
    x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    form = driver.find_element(By.CSS_SELECTOR, '#answer')
    form.send_keys(y)
    checkbox = driver.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    driver.execute_script('return arguments[0].scrollIntoView(true);', checkbox)
    checkbox.click()
    radio = driver.find_element(By.CSS_SELECTOR, '#robotsRule')
    driver.execute_script('return arguments[0].scrollIntoView(true);', radio)
    radio.click()
    button = driver.find_element(By.CSS_SELECTOR, 'button')
    driver.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    driver.quit()