import math

def alternating(n):
  sum_value = 0

  for i in range(n):
    numerator = (-1)**(i + 2)
    sum_value += (numerator / (i + 1))
  
  return sum_value

print(alternating(2))
print(alternating(4))
print(alternating(10))

def compound_interest(principal, rate, months):
  sum_value = principal

  for i in range(months):
    sum_value *= (1 + (rate / 12))

  return round(sum_value, 2)

print(compound_interest(100, 0.05, 6))
print(compound_interest(2500, 0.10, 3))

def regular_savings(deposit, rate, months):
  sum_value = 0

  for i in range(months):
    sum_value = (deposit + sum_value) * (1 + (rate / 12))

  return round(sum_value, 2)

print(regular_savings(100, 0.05, 6))

def sum_of_series(n):
  if (n < 1):
    return 0

  sum_value = 0

  for i in range(n):
    sum_value += (1 / ((i + 1)**2))
  
  return sum_value
  
print(sum_of_series(0))
print(sum_of_series(1))
print(sum_of_series(10))

for x in range(2, 25-1):
  print(x)

def is_prime(n):
  prime = True

  for i in range(2, n - 1):
    if (n % i == 0):
      prime = False
      
  return prime

print(is_prime(25))

def sum_of_series(n):
  if (n < 1):
    return 0

  sum_value = 0

  for i in range(n):
    sum_value += (1 / ((i + 1)**2))
  
  return sum_value

def fraction_of_pisq(s):
  return s / ((math.pi)**2 / 6)

def terms_required(p):
  n = 0
  frac = 0

  while (frac < p):
    n += 1
    sum_n_terms = sum_of_series(n)
    frac = fraction_of_pisq(sum_n_terms)
  
  return n

print(sum_of_series(6))
print(fraction_of_pisq(1.5))
print(terms_required(0.9))

def alternating_while(stop):
  sum_value = 0
  i = 1
  
  while (abs(1 / i) > stop):
    sum_value += (((-1)**(i + 1)) / i)
    i += 1
    
  return sum_value

print(alternating_while(0.249)) #0.5833333333333333
print(alternating_while(0.199)) #0.7833333333333332