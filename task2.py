import requests
import unittest
from unittest import TestCase


""" Статусы, требующие проверки
201 - ОК (успешное создание папки)
400 - Некорректные данные (отсутствие параметра path)
401 - Не авторизован (отсутствие заголовка)
409 - Ресурс "{path}" уже существует (повторное создание папки)
"""


class TestYandexDisk(TestCase):
    
    # Необходимо ввести собственный токен и название папки. 
    # После этого можно запустить тест.
    TOKEN = "y0_AaAAAAAAaAA8AAAAAaAAAAA-AOaaAAA_aaaA1AAAAaAAaAaA2AaAAAAA8A"
    FOLDER_NAME = "Netology_folder"
    
    
    def setup_api_link(self):
        return 'https://cloud-api.yandex.net/v1/disk/resources'
    
    
    def setup_headers(self):
        return {'Authorization': self.TOKEN}
    
    
    def setup_params(self):
        return {'path': self.FOLDER_NAME}
    
    
    def test_path_error(self):
        response = requests.put(self.setup_api_link(), headers = self.setup_headers())
        self.assertEqual(400, response.status_code)
    
    
    def test_headers_error(self):
        response = requests.put(self.setup_api_link(), params = self.setup_params())
        self.assertEqual(401, response.status_code)
    
    
    def test_create_folder(self):
        response = requests.put(self.setup_api_link(), headers = self.setup_headers(), 
                                params = self.setup_params())
        self.assertEqual(201, response.status_code)    
    
    
    def test_create_folder_again(self):
        response = requests.put(self.setup_api_link(), headers = self.setup_headers(), 
                                params = self.setup_params())
        self.assertEqual(409, response.status_code)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)