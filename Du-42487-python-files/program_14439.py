def get_price(age):
  if age <= 16:
    return "5"
  elif age > 60:
    return "7"
  else:
    return "10"

def merge_lists(l1,l2):
  l3 = []
  for lines in l1:
    i = 0
    while i <= len(l1):
      if i == 0 or i % 2 == 0:
        l3.append(l1[i])
        return l3
  

