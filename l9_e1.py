import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/redirect_accept.html"

try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(link)
    button = driver.find_element(By.CSS_SELECTOR,'.btn')
    button.click()
    confirm = driver.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x_element = driver.find_element(By.CSS_SELECTOR,'#input_value')
    x = x_element.text
    y = calc(x)
    form = driver.find_element(By.CSS_SELECTOR,'#answer')
    form.send_keys(y)
    button = driver.find_element(By.CSS_SELECTOR,'button')
    button.click()



finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    driver.quit()