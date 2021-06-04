import unittest
import pyalgo.math.euler

class TestEuler(unittest.TestCase):

    def test_gcd(self):
        result = pyalgo.math.euler.gcd(16, 72)
        answer = 8
        self.assertEqual(result, answer)

    def test_lcm(self):
        result = pyalgo.math.euler.lcm(16, 72)
        answer = 144
        self.assertEqual(result, answer)

    def test_totient(self):
        result = pyalgo.math.euler.totient(10)
        answer = 4
        self.assertEqual(result, answer)

if __name__ == "__main__":
    unittest.main()
