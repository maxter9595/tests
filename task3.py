import unittest
from unittest import TestCase

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class YandexAuthCheck:
    
    def __init__(self, username: str, password:str):
        """
        Переменные:
        username (str): имя пользователя Яндекс
        password (str): пароль пользователя Яндекс
        """
        self.username = username
        self.password = password
    
    def check_yandex_authorization(self) -> bool:
        """
        Вывод:
        authorization_bool (bool): фактический статус авторизации 
        пользователя (True - пользователь авторизирован, False -
        пользователь не авторизирован)
        """
        chrome_path = ChromeDriverManager().install()
        options = ChromeOptions()
        browser_service = Service(executable_path = chrome_path)

        yandex_url = "https://passport.yandex.ru/auth/"
        driver = Chrome(service = browser_service, options = options)
        driver.get(yandex_url)

        driver.find_element(By.ID, "passp-field-login").\
            send_keys(self.username)
        driver.find_element(By.ID, "passp:sign-in").click()

        try:
            WebDriverWait(driver = driver, timeout = 3).\
                until(EC.presence_of_element_located((
                        By.CLASS_NAME, "Field-errorIcon")))
            driver.close()
            return False
            
        except selenium.common.exceptions.TimeoutException:
            WebDriverWait(driver = driver, timeout = 3).\
                until(lambda driver: driver.current_url != yandex_url)
            driver.find_element(By.ID, "passp-field-passwd").\
                send_keys(self.password)
            driver.find_element(By.ID, "passp:sign-in").click()
            
            try:
                new_yandex_url = "https://passport.yandex.ru/auth/welcome"
                WebDriverWait(driver = driver, timeout = 10).\
                    until(lambda driver: driver.current_url != new_yandex_url)
                driver.close()
                return True
                
            except selenium.common.exceptions.TimeoutException:
                WebDriverWait(driver = driver, timeout = 3).\
                    until(EC.presence_of_element_located((
                            By.CLASS_NAME, "Field-errorIcon")))
                driver.close()
                return False


class YandexAuthTest(TestCase):

    def setUp(self):
        # Вводим почту пользователя, его пароль
        USERNAME = 'netology@yandex.ru'
        PASSWORD = 'NetologyPassword'
        self.yd_auth_check = YandexAuthCheck(USERNAME, PASSWORD)
    
    def tearDown(self):
        del self.yd_auth_check

    def test_yandex_authorization_check(self) -> None:
        # Вводим ожидаемый результат (True - пользователь 
        # авторизирован, False - наоборот)
        EXPECTED = True
        acutal = self.yd_auth_check.check_yandex_authorization()
        self.assertEqual(EXPECTED, acutal)


# Вызов теста
if __name__ == '__main__':
    unittest.main(verbosity=2)