def get_price(age):
  price = 0
  if int(age) <= 16:
     price = 5
  elif int(age) >= 60:
     price = 7
  else:
     price = 10
  return price


def merge_list(l1,l2):
  i = 0
  l3 = []
  while i < len(l1):
     l3.append(l1[i])
     i += 2
  j = 0
  while j < len(l2):
     l3.append(l2[i])
     j += 2
  
  return l3


def weird_case(some_str):
  string = some_str.split()
  i = 0
  new_string = []
  while i < len(string):
     j = 0
     word = string[i]
     while j < len(word):
        if j % 2 == 0:
           new_string.append(word[j].upper)
        else:
           new_string.append(word[j])
  return new_string
   


def remove_zeros(list):
   for n in list == 0:
      list.remove(0)
   



