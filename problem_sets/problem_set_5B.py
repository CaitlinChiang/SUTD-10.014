def increase_value(sample_dict, key):
  for i in sample_dict.keys():
    if (i == key):
      sample_dict[i] = sample_dict[i] + 1

  return sample_dict

print(increase_value({'apple': 100, 'banana':200}, 'apple'))
print(increase_value({7:10, 8:40}, 3))

def translate_point(dd, key, vector):
  tuple_dictionary = {}

  for i in dd.keys():
    if (i == key):
      tuple_dictionary[i] = (dd[i][0] + vector[0], dd[i][1] + vector[1])
    else: 
      tuple_dictionary[i] = dd[i]

  return tuple_dictionary

print(translate_point({'A': (1,2), 'B': (-3,4), 'C': (-1,2)}, 'A', (3, 2)))
print(translate_point({'F': (1,2), 'G': (-3,4), 'H': (-1,2)}, 'D', (3, 2)))

def translate_point_new(dd, key, vector):
  tuple_dictionary = {}

  for i in dd.keys():
    if (i == key):
      tuple_dictionary[i] = (dd[i][0] + vector[0], dd[i][1] + vector[1])
    else: 
      tuple_dictionary[i] = dd[i]

  return tuple_dictionary

dd = {'A': (1,2), 'B': (-3,4), 'C': (-1,2)}
key = 'A'
vector = (3, 2)
d_new = translate_point_new(dd, key, vector)
print(dd)
print(d_new)
print(dd is d_new)

def replace_values(ls, value1, value2):
  if (value1 not in ls):
    return ls
  
  newlist = []

  for i in ls:
    if (i == value1):
      newlist.append(value2)
    else:
      newlist.append(i)

  return newlist

print(replace_values([3, 9, 5, 10, 2, 4, 10, 3], 3, 12))
print(replace_values([4, 9, 5, 10, 2, 4, 10, 4], 3, 12))

def replace_values(ls, value1, value2):
  newlist = ls.copy()

  for i in range(len(ls)):
    if (newlist[i] == value1):
      newlist[i] = value2

  return newlist

ls1 = [3, 9, 5, 10, 2, 4, 10, 3]
ls2 = replace_values(ls1, 3, 12)
print("ls1", ls1)
print("ls2", ls2)

ls3 = [4, 9, 5, 10, 2, 4, 10, 4]
ls4 = replace_values(ls3, 3, 12)
print("ls3", ls3)
print("ls4", ls4)

def equation_of_line(point1, point2):
  a = point2[0] - point1[0]
  b = - (point2[1] - point1[1])
  c = (point1[0] * (point2[1] - point1[1])) - (point1[1] * a)

  return a, b, c

def reflect(point, eqn):
  p = point[0]
  q = point[1]
  a = eqn[0]
  b = eqn[1]
  c = eqn[2]

  p_numerator = (p * ((a**2) - (b**2))) - (2 * b * ((a * q) + c))
  q_numerator = (q * ((b**2) - (a**2))) - (2 * a * ((b * p) + c))
  denominator = (a**2) + (b**2)

  return (p_numerator / denominator), (q_numerator / denominator)

def reflect_triangle(dd, point):
  temporary_array = []
  reflection_dict = {}
  point_key = ''
  point_value = ()

  for i in dd.keys():
    if (i == point):
      point_key = i
      reflection_dict[i] = ()
      point_value = dd[i]
    else:
      temporary_array.append(dd[i])
      reflection_dict[i] = dd[i]
  
  reflection_dict[point_key] = reflect(point_value, equation_of_line(temporary_array[0], temporary_array[1]))

  return reflection_dict
    
print(reflect_triangle({'A': (1,2), 'B': (-3,4), 'C': (-1,2)}, 'B'))
