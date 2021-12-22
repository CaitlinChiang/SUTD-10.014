def create_dictionary(fruits, prices):
  if (len(fruits) != len(prices)):
    return None

  fruits_dictionary = {}
  
  for i in range(len(fruits)):
    fruits_dictionary[fruits[i]] = prices[i]

  return fruits_dictionary

print(create_dictionary(['apple', 'orange'], [0.43, 0.51]))
print(create_dictionary(['apple'], [0.43, 0.51]))

def get_value(sample_dict, key):
  if (key in sample_dict):
    return sample_dict[key]
  else: 
    return None

print(get_value({1:2, 2:3}, 2))
print(get_value({1:2, 2:3}, 3))

import math

def extract_data(dd, key):
  if (key in dd):
    return round(math.sqrt((dd[key][0]**2) + (dd[key][1]**2)), 2)
  else:
    return None

print(extract_data({'A': (1,2), 'B': (-3,4), 'C': (-1,2)}, 'A'))
print(extract_data({'A': (1,2), 'B': (-3,4), 'C': (-1,2)}, 'D'))

def get_base_counts(dna):
  non_dna = False

  a_counter = 0
  c_counter = 0
  g_counter = 0
  t_counter = 0

  for i in dna:
    if (i == 'A'):
      a_counter += 1
    elif (i == 'C'):
      c_counter += 1
    elif (i == 'G'):
      g_counter += 1
    elif (i == 'T'):
      t_counter += 1
    else: 
      non_dna = True

  if (non_dna):
    return 'The input DNA string is invalid'

  return { 'A': a_counter, 'C': c_counter, 'G': g_counter, 'T': t_counter }

print(get_base_counts('AACCCGT'))
print(get_base_counts('AACCG'))
print(get_base_counts('AAB'))

def evaluate_polynomial(dd, x):
  sum_value = 0

  for i in dd.keys():
    if (i == 0):
      sum_value += dd[i]
    else:
      sum_value += (x * dd[i]) ** i

  return round(sum_value, 2)

print(evaluate_polynomial({3:1, 1:2, 0:1}, 0.5))

def diff(pp):
  dp = {}

  for i in pp.keys():
    if (i != 0):
      dp[i - 1] = i * pp[i]
  
  return dp

print(diff({0:-3, 3:2, 5:-1}))

def read_list(ls, reg_no, key):
  for i in range(len(ls)):
    if (ls[i]['reg'] == reg_no):
      if (ls[i].get(key) == None):
        return None
      else:
        return ls[i][key]

ls = [
  {'reg': '1234A', 'make':'Caelum', 'price': 24999}, 
  {'reg': '888B', 'make':'Noctis', 'price': 12499}, 
  {'reg': '365K', 'make':'Cloud', 'price': 7499},
  {'reg': '1043W', 'price': 2499}, 
  {'reg': '7422M', 'make': 'Lucis'} 
]

print(read_list(ls, '888B', 'make'))
print(read_list(ls, '7422M', 'price'))

def get_highest_value(dd):
  maximum_key = max(dd, key = dd.get)
  return (maximum_key, dd[maximum_key])

print(get_highest_value({'a': 123, 'b': 132, 'c': 95}))
