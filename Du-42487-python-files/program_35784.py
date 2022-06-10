def get_price(age):
  if age < 16:
    return "5 euro"
  elif 60 > age:
    return "7 euro"
  else:
    return "10 euro"

def merge_lists(l1,l2):
  l3 =[]
  i = 0
  while i < len(l1):
    if i % 2 == 0:
      l3.append(l1[i])
    i = i + 1
  j = 0
  while j < len(l2):
    if j % 2 == 0:
      l3.append(l2[i])
    j = j + 1
  return l3

def weird_case(some_str):
  i = 0
  while i < len(some_str):
    if i % 2 == 0:
      some_str[i] = some_str[i].upper()
    i = i + 1
  return some_str

def remove_zeros(list):
  i = 0
  while i < len(list):
    list.remove(0)
    i = i + 1
