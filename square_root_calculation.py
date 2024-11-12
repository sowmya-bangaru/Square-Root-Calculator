import math
def square_root_calculation(num):
  if num < 0:
    print("provided input is negative")
    raise ValueError("input must be non-negative")
  return math.sqrt(num)
