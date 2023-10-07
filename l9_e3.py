import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/cats.html"

try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(5) # Неявное ождиание, чтобы не уронить тест случайно из-за скрипта или инета
    driver.get(link)
    driver.find_element(By.ID, "button")


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    driver.quit()