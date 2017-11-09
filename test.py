import unittest

import maths_custom_functions as mcf


class TestMathsCustomFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(mcf.factorial(0), 1)
        self.assertEqual(mcf.factorial(1), 1)
        self.assertEqual(mcf.factorial(2), 2)
        self.assertEqual(mcf.factorial(15), 1307674368000)

    def test_is_perfect_number(self):
        self.assertTrue(mcf.is_perfect_number(6))
        self.assertTrue(mcf.is_perfect_number(28))
        self.assertTrue(mcf.is_perfect_number(496))
        self.assertTrue(mcf.is_perfect_number(8128))

        self.assertFalse(mcf.is_perfect_number(0))
        self.assertFalse(mcf.is_perfect_number(1))
        self.assertFalse(mcf.is_perfect_number(2))
        self.assertFalse(mcf.is_perfect_number(12345))

        self.assertRaisesRegexp(ValueError, "The number .+ is negative!", mcf.is_perfect_number, -1)

    def test_fibonacci(self):
        self.assertEqual(mcf.fibonacci(0), 1)
        self.assertEqual(mcf.fibonacci(1), 1)
        self.assertEqual(mcf.fibonacci(2), 2)
        self.assertEqual(mcf.fibonacci(15), 987)

if __name__ == '__main__':
    unittest.main()
