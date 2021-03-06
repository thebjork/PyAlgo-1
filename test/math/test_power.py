import pyalgo.math.power
import unittest

class TestPower(unittest.TestCase):

    def test_power(self):

        result = pyalgo.math.power.power(50, 25)
        answer = 2980232238769531250000000000000000000000000
        self.assertEqual(result, answer)

if __name__ == "__main__":
    unittest.main()
