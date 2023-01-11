from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class yandex_loginer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.start_url = 'https://passport.yandex.ru/auth/'
        cls.login = '' # Логин яндекса
        cls.password = '' # Пароль
        cls.driver.get(cls.start_url)

    @classmethod
    def TearDownClass (cls):
        cls.driver.close()

    def test_login (self):
        elem = self.driver.find_element(By.XPATH,"//button[@data-type='login']")
        elem.click()
        elem = self.driver.find_element(By.NAME,'login')
        elem.send_keys(self.login)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertEqual( 'https://passport.yandex.ru/auth/welcome',self.driver.current_url)

    def test_password (self):
        elem = self.driver.find_element(By.ID,'passp-field-passwd')
        elem.send_keys(self.password)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertEqual('https://id.yandex.ru/',self.driver.current_url)

if __name__ == '__main__':
    unittest.main()