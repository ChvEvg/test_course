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
    driver.implicitly_wait(5) # Неявное ождиание, чтобы не уронить тест случайно из-за скрипта или инета
    driver.get(link)


    button = driver.find_element(By.CSS_SELECTOR,'.btn')
    button.click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
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