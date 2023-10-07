import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/huge_form.html"

try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(link)
    elements = driver.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("1")

    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(5)
    driver.quit()