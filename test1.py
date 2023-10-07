import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

time.sleep(5)

driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)


textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

textarea.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

submit_button.click()
time.sleep(5)

driver.quit()