import unittest

import maths_custom_functions as mcf


class TestMathsCustomFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(mcf.factorial(0), 1)
        self.assertEqual(mcf.factorial(1), 1)
        self.assertEqual(mcf.factorial(2), 2)
        self.assertEqual(mcf.factorial(15), 1307674368000)


if __name__ == '__main__':
    unittest.main()
