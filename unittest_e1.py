import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class TestLogin(unittest.TestCase):
    def test_login_1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        driver  = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(link)
        f_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
        f_name.send_keys('IVAN')
        l_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        l_name.send_keys('IVANOV')
        email = driver.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
        email.send_keys('ivivanov@mail.ru')
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'No welcome text')

    def test_login_2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        driver  = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(link)
        f_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
        f_name.send_keys('IVAN')
        l_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        l_name.send_keys('IVANOV')
        email = driver.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
        email.send_keys('ivivanov@mail.ru')
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'No welcome text')

if __name__ == '__main__':
    unittest.main()
    