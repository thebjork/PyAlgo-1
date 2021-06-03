import pyalgo.math.sieve
import unittest

class TestSieve(unittest.TestCase):

    def test_sieve(self):

        result = pyalgo.math.sieve.sieve(10)
        answer = [2, 3, 5, 7]
        self.assertEqual(result, answer)

if __name__ == "__main__":
    unittest.main()
