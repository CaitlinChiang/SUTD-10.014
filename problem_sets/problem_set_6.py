def get_average_sublist(ls, n):
  if (n > 0 and n >= len(ls)):
    return None
  elif (n < 0 and abs(n) > len(ls)):
    return None

  sum_value = 0

  for i in ls[n]:
    sum_value += i

  return round(sum_value / len(ls[n]), 1)

a = [[10, 12], [36, 40, 52], [10, 16, 17]] 
print(get_average_sublist(a, -3))
print(get_average_sublist(a, 3))

def has_list(ls):
  list_exists = False

  for element in ls:
    if (type(element) is list):
      list_exists = True
  
  return list_exists

print(has_list([10, 20, [30, 40] , 'apple' ]))
print(has_list([10, 20, 30, 40 , 'apple' ]))

def max_list(inlist):
  outlist = []

  for i in inlist:
    outlist.append(max(i))

  return outlist

print(max_list([[1, 2, 3],[4, 5]]))
print(max_list([[3, 4, 5, 2],[1, 7], [8, 0, -1], [2]]))
print(max_list([[3, 4, 5, 2]]))

def find_average(ls):
  total_average = 0
  number_of_elements = 0

  sublist_outlist = []

  for sublist in ls:
    sublist_average = 0

    for j in sublist:
      sublist_average += j
      total_average += j
      number_of_elements += 1

    sublist_outlist.append(round(sublist_average / len(sublist), 2))

  return sublist_outlist, round((total_average / number_of_elements), 2)

print(find_average([[3,4],[5,6,9], [-1,2,8]]))

def get_zero_matrix(m, n):
  m_array = []

  for j in range(m):
    n_array = []
    n_array.extend([0] * n)
    m_array.append(n_array)

  return m_array

print(get_zero_matrix(1, 4))
print(get_zero_matrix(3, 1))

def transpose_matrix(ls):
  rows = len(ls)
  columns = len(ls[0])
  sublist_count = 0

  updated_matrix = get_zero_matrix(columns, rows)

  for sublist in ls:
    for i in range(columns):
      updated_matrix[i][sublist_count] = sublist[i]

    sublist_count += 1

  return updated_matrix
  
print(transpose_matrix([[1, 2, 3], [40, 50, 60]]))

def process_scores(f):
  fstring = f.read()

  total = 0

  for i in fstring.split():
    total += int(i)

  return total, round((total / len(fstring.split())), 1)

with open('../additional_files/scores.txt', 'r') as f:
  out = process_scores(f)
  print(out)

def read_fdi(f):
  file_data = f.read()
  rows = file_data.split("\n")

  fdi_data = {}

  for row in rows[1 : - 1]:
    info = row.split(",")
    fdi_data[info[0]] = float(info[2])

  return fdi_data

with open('../additional_files/fdi.csv', 'r') as f:
  data = read_fdi(f)
  print(data)

def gc_content(f):
  file_data = f.read()
  rows = file_data.split("\n")

  bases = 0
  total = 0

  for row in rows:
    for i in row: 
      if (i == 'G' or i == 'C'):
        bases += 1
      total += 1
  
  return round((bases / total) * 100, 1)

with open('../additional_files/dna.txt', 'r') as f:
  solution = gc_content(f)
  print(solution)

def scalar_multiply(ls, a):
  for sublist in range(len(ls)):
    for i in range(len(ls[sublist])): 
      ls[sublist][i] = ls[sublist][i] * a

  return ls

A = [[10, 20, 30], [40, 50, 60]]
scalar_multiply(A, 0.2)
print(A)

def scalar_multiply_new(ls, a):
  new_array = []

  for sublist in ls:
    sublist_array = []

    for i in sublist:
      sublist_array.append(i * a)

    new_array.append(sublist_array)

  return new_array

A = [ [10, 20, 30 ] ,
      [40, 50, 60] ]
B = scalar_multiply_new(A, 0.2)
print(A)
print(B)