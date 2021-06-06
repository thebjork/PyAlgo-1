import pyalgo.math.gray_code
import unittest

class TestGrayCode(unittest.TestCase):

    def test_gray_code(self):

        result = pyalgo.math.gray_code.gray_code(3)
        answer = ['000', '001', '011', '010', '110', '111', '101', '100']
        self.assertEqual(result, answer)

if __name__ == "__main__":
    unittest.main()
