import pytest
import math
import sys
from io import StringIO
from unittest.mock import patch
from square_root_calculation import square_root_calculation

# Test the square_root_calculation function
def test_square_root_calculation():
    # Test with a positive number
    result = square_root_calculation(4)
    assert result == 2.0, f"Expected 2.0, but got {result}"

    # Test with zero
    result = square_root_calculation(0)
    assert result == 0.0, f"Expected 0.0, but got {result}"

    # Test with a non-perfect square
    result = square_root_calculation(2)
    assert result == pytest.approx(math.sqrt(2), rel=1e-9), f"Expected {math.sqrt(2)}, but got {result}"

    # Test with a negative number (should raise ValueError)
    with pytest.raises(ValueError, match="Input must be non-negative"):
        square_root_calculation(-1)

# Test the argparse part (simulating command-line input)
@patch('sys.argv', ['square_root_calculation.py', '16'])
@patch('sys.stdout', new_callable=StringIO)
def test_script_square_root(mock_stdout, mock_argv):
    # Import the script (which will execute the code)
    import square_root_calculation

    # Check if the output is correct
    output = mock_stdout.getvalue().strip()
    expected_output = "The square root of 16.0 is 4.0"
    assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"

@patch('sys.argv', ['square_root_calculation.py', '25'])
@patch('sys.stdout', new_callable=StringIO)
def test_script_square_root_with_different_input(mock_stdout, mock_argv):
    # Import the script (which will execute the code)
    import square_root_calculation

    # Check if the output is correct
    output = mock_stdout.getvalue().strip()
    expected_output = "The square root of 25.0 is 5.0"
    assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"

# Test the script for negative input
@patch('sys.argv', ['square_root_calculation.py', '-9'])
@patch('sys.stdout', new_callable=StringIO)
def test_script_with_negative_input(mock_stdout, mock_argv):
    # Import the script (which will execute the code)
    import square_root_calculation

    # Check if the error message is correct
    output = mock_stdout.getvalue().strip()
    expected_output = "Error: Input must be non-negative"
    assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"
