def median(ls):
  ls.sort()
  even = len(ls) % 2 == 0

  if (even):
    middle_values = int(len(ls) / 2)
    return (ls[middle_values] + ls[middle_values - 1]) / 2
  else:
    middle_value = int((len(ls) / 2) - 0.5)
    return ls[middle_value]

print(median([5, 7, 3, 8, 6]))
print(median([5, 7, 3, 8, 6, 9]))

def middle_list(ls):
  return ls[1:-1]

print(middle_list([1, 9]))
print(middle_list([1, 9, 4]))

def swap_elements(ls, index1, index2):
  newlist = []

  if ((index1 > 0 and index1 >= len(ls)) or ((index2 > 0 and index2 >= len(ls)))):
    return None

  if ((index1 < 0 and index1 > len(ls)) or ((index2 < 0 and index2 > len(ls)))):
    return None
  
  for i in ls:
    if (i == ls[index1]):
      newlist.append(ls[index2])
    elif (i == ls[index2]):
      newlist.append(ls[index1])
    else:
      newlist.append(i)
  
  return newlist

ls = [3, 6, 8, 7]
newls1 = swap_elements(ls, -4, -2)
print(newls1)
print(newls1 is ls)
newls2 = swap_elements(ls, -3, -1)
print(newls2)
result = swap_elements(ls, 3, 4)
print(result)

def sum_odd_numbers(ls):
  sum_value = 0

  for i in ls:
    if (i % 2 == 1 and i > 0):
      sum_value += i

  return sum_value

print(sum_odd_numbers([1, 2, 3]))
print(sum_odd_numbers([43, 30, 27, -3]))

def hailstone(n):
  sequence_list = []
  sequence_list.append(n)

  while n > 1:
    if (n % 2 == 0):
      n = n/2
      sequence_list.append(int(n))
    else:
      n = (3*n) + 1
      sequence_list.append(int(n))

  return sequence_list

print(hailstone(4))
print(hailstone(5))

def get_odd_numbers(ls):
  ls.sort()
  
  odd_list = []

  for i in ls:
    if (i % 2 == 1):
      odd_list.append(i)

  return odd_list

print(get_odd_numbers([3, 2, 1]))
print(get_odd_numbers([43, 30, 27, -3]))

def moving_average(ls):
  average_list = []
  n = 0

  while ((n + 3) <= len(ls)):
    average = (ls[n] + ls[n + 1] + ls[n + 2]) / 3
    average_list.append(round(average, 1))
    n += 1

  return average_list

print(moving_average([30.0, 20.0, 40.0, 50.0, 25.0, 70.0]))

def trapezoidal_rule(f, dx):
  array_length = len(f)

  if (array_length <= 1):
    return 0

  n = dx / 2
  series_sum = 0

  for i in f: 
    if (i == f[0] or i == f[-1]):
      series_sum += i
    else:
      series_sum += (2 * i)

  return n * series_sum

print(trapezoidal_rule([3.5, 7.8, 11.0, 9.0, 3.0], 2))

def left_riemann_sum(x, y):
  array_length = len(x)

  if (array_length <= 1):
    return 0
  
  total_area = 0
  n = 0

  for i in range((len(x) - 1)):
    area = (x[n + 1] - x[n]) * (y[n])
    total_area += area
    n += 1

  return total_area

x = [0, 2, 3, 5, 6]
y = [1, 1.5, 1.7, 1.9, 2.0]
print(left_riemann_sum(x, y))
