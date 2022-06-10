#Test 1
def get_price(age):
  if age <= 16:
    return "5"
  elif age > 60:
    return "7"
  else:
    return "10"

#Test 2
def merge_lists(l1,l2):
  l3 = []
  for lines in l1, l2:
    l3 = l1[::2] + l2[::2]
    return l3

#Test 3


#Test 4
def remove_zeros(listy):
  i = 0
  for numbers in listy:
    if 0 in listy:
      listy.remove(0)
