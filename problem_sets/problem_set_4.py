def calculate_bmi(weight, height):
  height = height / 100
  bmi = weight / (height**2)
  rounded_bmi = round(bmi, 1)
  return rounded_bmi

def describe_bmi(bmi):
  if (bmi < 18.5):
    return 'nutritional deficiency'
  elif (bmi >= 18.5 and bmi < 23):
    return 'low risk'
  elif (bmi >= 23 and bmi < 27.5):
    return 'moderate risk'
  else:
    return 'high risk'

def bmi_information(weight, height):
  return "Your BMI is {bmi} and your category is {description}.".format(bmi = calculate_bmi(weight, height), description = describe_bmi(calculate_bmi(weight, height)))

print(bmi_information(70, 167))

def reverse(s):
  return s[::-1]

print(reverse('I choose you'))

def is_palindrome(s):
  return s == s[::-1]

print(is_palindrome('civic'))
print(is_palindrome('sonar'))

def match(ending, word):
  return word.endswith(ending)

ending = 'nus'
word = 'parvenus' 
result = match(ending, word)
print(result)

ending = 'nus'
word = 'aviatrix'
result = match(ending, word)
print(result)

ending = 'lar'
word = 'agricolarum'
result = match(ending, word)
print(result)

def check_password(pwd):
  check_length = len(pwd) >= 8
  check_characters = True
  
  digits = 0
  for i in pwd:
    if (not i.isalpha() and not i.isnumeric()):
      check_characters = False

    if (i.isnumeric()):
      digits += 1

  check_digits = digits >= 2

  return check_length and check_characters and check_digits

print(check_password('test'))
print(check_password('testtest'))
print(check_password('testt22'))
print(check_password('testte22'))

def longest_common_prefix(s1, s2):
  prefix = ''
  n = 0

  for i in s1:
    if (s1[n] == s2[n]):
      prefix += i
    else:
      break

    n += 1

  return prefix

print(longest_common_prefix('distance', 'disinfection'))
print(longest_common_prefix('testing', 'technical'))
print(longest_common_prefix('rosses', 'crosses'))

def binary_to_decimal(s):
  return int(s, 2)

print(binary_to_decimal('100'))  
print(binary_to_decimal('101'))  
print(binary_to_decimal('10001'))  
print(binary_to_decimal('10101'))

def uncompressed(s):
  final_string = ''
  n = 0

  while (n < len(s)):
    letter = s[n + 1]
    for j in range(int(s[n])):
      final_string += letter
    n += 2

  return final_string

print(uncompressed('1x1y'))
print(uncompressed('2a5b1c'))
print(uncompressed('1a1b2c'))
print(uncompressed('1a9b3b1c'))

def get_base_counts(dna):
  dna_count = []
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
    return dna_count
  else:
    return [a_counter, c_counter, g_counter, t_counter]

print(get_base_counts('AACCCGT'))
print(get_base_counts('AACCG'))
print(get_base_counts('AAB'))