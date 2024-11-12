import math
import argparse

def square_root_calculation(num):
    # Check if the input number is non-negative
    if num < 0:
        raise ValueError("Input must be non-negative")
    return math.sqrt(num)

# Setup argument parser
parser = argparse.ArgumentParser(description="Calculate the square root of a number.")
parser.add_argument('number', type=float, help="The number for which you want to calculate the square root.")

# Parse command-line arguments
args = parser.parse_args()

try:
    # Call the function to calculate the square root
    result = square_root_calculation(args.number)
    
    # Display the result
    print(f"The square root of {args.number} is {result}")
    
except ValueError as e:
    # Handle invalid input or negative numbers
    print(f"Error: {e}")
