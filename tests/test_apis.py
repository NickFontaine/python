import unittest
import requests
import json
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    def test_no_pets(self):
        r = requests.get("https://petstore.swagger.io/v2/pet/1")
        print(r.status_code)
        assert r.status_code == 404

if __name__ == "__main__":
    unittest.main()

