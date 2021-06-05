from typing import Union
import unittest
import requests

URL = "https://pyalgo-api.herokuapp.com"

class TestAPI(unittest.TestCase):

    def test_status(self):
        DATA = requests.get(url = URL)
        RESULT = "PyAlgo API is working"
        self.assertEqual(RESULT, DATA.json())

    def test_factorial(self):
        DATA = requests.get(url = f"{URL}/math/factorial?number=10")
        RESULT = 3628800
        self.assertEqual(RESULT, DATA.json())

    def test_sieve(self):
        DATA = requests.get(url = f"{URL}/math/sieve?number=10")
        RESULT = [2, 3, 5, 7]
        self.assertEqual(RESULT, DATA.json())

    def test_gray_code(self):
        DATA = requests.get(url = f"{URL}/math/graycode?number=2")
        RESULT = ["00", "01", "11", "10"]
        self.assertEqual(RESULT, DATA.json())

    def test_gcd(self):
        DATA = requests.get(url = f"{URL}/math/gcd?num1=16&num2=72")
        RESULT = 8
        self.assertEqual(RESULT, DATA.json())

    def test_lcm(self):
        DATA = requests.get(url = f"{URL}/math/lcm?num1=16&num2=72")
        RESULT = 144
        self.assertEqual(RESULT, DATA.json())

    def test_totient(self):
        DATA = requests.get(url = f"{URL}/math/totient?number=10")
        RESULT = 4
        self.assertEqual(RESULT, DATA.json())

    def test_power(self):
        DATA = requests.get(url = f"{URL}/math/power?num1=50&num2=25")
        RESULT = 2980232238769531250000000000000000000000000
        self.assertEqual(RESULT, DATA.json())

if __name__ == "__main__":
    unittest.main()
