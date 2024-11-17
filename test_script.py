import pytest
import math
from square_root_calculation import square_root_calculation  # Replace 'your_script' with the actual script filename

# Test for normal valid inputs
def test_positive_number():
    result = square_root_calculation(16)
    assert result == 4, f"Expected 4 but got {result}"

def test_positive_decimal():
    result = square_root_calculation(2.25)
    assert result == 1.5, f"Expected 1.5 but got {result}"

# Test for edge case with zero
def test_zero():
    result = square_root_calculation(0)
    assert result == 0, f"Expected 0 but got {result}"

# Test for a negative number which should raise ValueError
def test_negative_number():
    with pytest.raises(ValueError, match="input must be non-negative"):
        square_root_calculation(-9)

# Test for large number
def test_large_number():
    result = square_root_calculation(1e6)
    assert result == 1000, f"Expected 1000 but got {result}"

# Test for small positive number (close to zero)
def test_small_positive():
    result = square_root_calculation(1e-6)
    assert math.isclose(result, 1e-3), f"Expected {1e-3} but got {result}"

