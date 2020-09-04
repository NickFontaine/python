import unittest
import requests
import json

class Test(unittest.TestCase):

    def test_delete_user(self):
        url = requests.delete("https://reqres.in/api/users/2")
        print("User was deleted: " + str(url.status_code))
        assert url.status_code == 204

if __name__ == "__main__":
    unittest.main()

