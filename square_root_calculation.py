import math
def square_root_calculation(num):
  if num < 0:
    raise ValueError("input must be non-negative")
  return math.sqrt(num)

