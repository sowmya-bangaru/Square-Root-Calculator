import unittest
import math
from square_root_calculation import square_root_calculation

class TestSquareRootCalculation(unittest.TestCase):

    # Test for valid positive numbers
    def test_positive_number(self):
        result = square_root_calculation(16)
        self.assertEqual(result, 4, f"Expected 4 but got {result}")
        
    def test_positive_decimal(self):
        result = square_root_calculation(2.25)
        self.assertEqual(result, 1.5, f"Expected 1.5 but got {result}")

    # Test for edge case with zero
    def test_zero(self):
        result = square_root_calculation(0)
        self.assertEqual(result, 0, f"Expected 0 but got {result}")

    # Test for a negative number should raise ValueError
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            square_root_calculation(-9)

    # Test for large numbers
    def test_large_number(self):
        result = square_root_calculation(1e6)
        self.assertEqual(result, 1000, f"Expected 1000 but got {result}")

    # Test for small positive number (close to zero)
    def test_small_positive(self):
        result = square_root_calculation(1e-6)
        self.assertTrue(math.isclose(result, 1e-3), f"Expected {1e-3} but got {result}")

if __name__ == "__main__":
    unittest.main()
