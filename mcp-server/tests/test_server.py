import unittest
from src.server import app

class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_sum_numbers(self):
        response = self.app.get('/sum?num1=3&num2=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 8)

if __name__ == '__main__':
    unittest.main()