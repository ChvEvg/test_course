import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/selects1.html"

try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(link)
    x_element = driver.find_element(By.CSS_SELECTOR, '#num1')
    x = x_element.text
    y_element = driver.find_element(By.CSS_SELECTOR, '#num2')
    y = y_element.text
    sum = str(eval(''.join([x,'+',y])))
    select = Select(driver.find_element(By.CSS_SELECTOR, 'select'))
    select.select_by_visible_text(sum)
    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    driver.quit()