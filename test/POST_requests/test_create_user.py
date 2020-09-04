import unittest
import requests
import json


class Test(unittest.TestCase):

    def test_add_user(self):
        url = "https://reqres.in/api/users"
        file = open("/Applications/Python/python/test_files/user.json", "r")
        json_input = file.read()
        request_json = json.loads(json_input)

        response = requests.post(url, request_json)

        print(response.status_code)
        print(response.text)
        assert response.status_code == 201

if __name__ == "__main__":
    unittest.main()

