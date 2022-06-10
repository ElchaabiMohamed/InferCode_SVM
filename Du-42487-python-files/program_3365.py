def get_price(age):
  if age <= 16:
    return "5"
  elif age >= 60:
    return "7"
  else:
    return "10"

	
def merge_lists(l1,l2):
  a = []
  i = 0
  while i < len(l1):
    a.append(l1[i])
    i = i + 2
  j = 0
  while j < len(l2):
    a.append(l2[j])
    j = j + 2 
  return a
  
def weird_case(some_str):
  i = 0 
  while i < len(some_str):
    tokens = some_str.split()
  i = i + 1 
  return tokens