import unittest
from ankurhello.math_operations import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        # Test case 1: Adding two positive numbers
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

        # Test case 2: Adding a positive and a negative number
        result = add_numbers(-5, 3)
        self.assertEqual(result, -2)

        # Test case 3: Adding two negative numbers
        result = add_numbers(-5, -3)
        self.assertEqual(result, -8)

        # Test case 4: Adding two floats
        result = add_numbers(2.5, 3.5)
        self.assertEqual(result, 6.0)

        # Test case 5: Adding an integer and a float
        result = add_numbers(2, 3.5)
        self.assertEqual(result, 5.5)

if __name__ == '__main__':
    unittest.main()
