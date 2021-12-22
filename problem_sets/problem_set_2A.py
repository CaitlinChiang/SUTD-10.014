def calculate_bmi(weight, height):
  height = height / 100
  bmi = weight / (height**2)
  rounded_bmi = round(bmi, 1)
  return rounded_bmi

print (calculate_bmi (2.5,50))
print (calculate_bmi (50 ,150))
print (calculate_bmi (43.5 ,142.3))

def position_velocity(vo, t):
  g = 9.81
  position = round((vo*t) - (g*(t**2) / 2), 3)
  velocity = round(vo - (g*t), 3)
  return position, velocity

print(position_velocity(5.0, 0))
print(position_velocity(10.0, 1))
print(position_velocity(5.886, 0.3))


import math
from math import e

def decay(a, t):
  x = (e**(0 - (a*t))) * math.cos(a*t)
  return x

print(decay(2, 0))
print(decay(2, 0.5))

def describe_bmi(bmi):
  if (bmi < 18.5):
    return 'nutritional deficiency'
  elif (bmi >= 18.5 and bmi < 23):
    return 'low risk'
  elif (bmi >= 23 and bmi < 27.5):
    return 'moderate risk'
  else:
    return 'high risk'

print(describe_bmi(18))
print(describe_bmi(20)) 
print(describe_bmi(24))
print(describe_bmi(27.5))

def is_positive_even(n):
  return n > 0 and n % 2 == 0

print(is_positive_even(-2))
print(is_positive_even(2))
print(is_positive_even(3))

def letter_grade(mark):
  if (mark >= 0 and mark < 60):
    return 'E'
  elif (mark >= 60 and mark <= 69):
    return 'D'
  elif (mark >= 70 and mark <= 79):
    return 'C'
  elif (mark >= 80 and mark <= 89):
    return 'B'
  elif (mark >= 90 and mark <= 100):
    return 'A'

print(letter_grade(102))
print(letter_grade(100))
print(letter_grade(83)) 
print(letter_grade(75))
print(letter_grade(67))
print(letter_grade(52))
print(letter_grade(-2))

def largest_area(s, u, v):
  if (s < 0 or u < 0 or v < 0):
    return None
  elif (u > s or v > s):
    return None
  else: 
    area_1 = v * u
    area_2 = (s - v) * u
    area_3 = (s - u) * v
    area_4 = (s - u) * (s - v)
    lst = [area_1, area_2, area_3, area_4]
    return max(lst)

result = largest_area(10, 3, 4)
print(result)
result = largest_area(10, 11, 4)
print(result)
result = largest_area(-10, 3, 4)
print(result)
