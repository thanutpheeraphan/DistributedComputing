from server import app
import unittest
import requests


class TestServer(unittest.TestCase):
    
    URL = "http://0.0.0.0:8080/email"
    
    API_JSON = {
    "email": "61090045@kmitl.ac.th"
    }
    

    def test_post(self):
        r = requests.post(TestServer.URL, json=TestServer.API_JSON)
        self.assertEqual(r.status_code,200)



if __name__ == "__main__":
    unittest.main()
