import math
def calculate_square_root(num):
  if num < 0:
    print("provided input is negative")
    raise ValueError("input must be non-negative")
  return math.sqrt(num)
