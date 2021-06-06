import pyalgo.math.factorial
import unittest

class TestFacroial(unittest.TestCase):

    def test_factorial(self):

        result = pyalgo.math.factorial.factorial(50)
        answer = 30414093201713378043612608166064768844377641568960512000000000000
        self.assertEqual(result, answer)

if __name__ == "__main__":
    unittest.main()
