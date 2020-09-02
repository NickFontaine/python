import unittest
import requests
import json
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    def test_no_pets(self):
        url = requests.get("https://reqres.in/api/users/1")
        print("User was found: " + str(url.status_code))
        assert url.status_code == 200

if __name__ == "__main__":
    unittest.main()

