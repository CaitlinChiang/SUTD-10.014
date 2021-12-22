import math

def sequence(n):
  fraction = ((2*n) + 1) / (n + 3)

  if (n < -0.5 and n >= -3):
    return None
  else: 
    return round(math.sqrt(fraction), 4)

print(sequence(-4.0))
print(sequence(-2.0))
print(sequence(0.0))
print(sequence(2.0))

def check_value(n1, n2, n3, x):
  return x > n1 and x > n2 and x < n3

print(check_value(1, 4, 8, 7))
print(check_value(10, 4, 8, 7))
print(check_value(1, 10, 8, 7))
print(check_value(1, 4, 5, 7))