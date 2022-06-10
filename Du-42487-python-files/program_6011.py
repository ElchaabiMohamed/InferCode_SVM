def get_price(age):
  if int(age) <= 16:
    return 5
  elif int(age) >= 60:
    return 7
  else:
    return 10

if __name__ == '__main__':
   print('calling get_price(age)')
   print(get_price(21))

def merge_list(l1,l2):
  l3 = []
  i = 0
  while i < len(l1):
    l3.append(l1[i])
    i = i + 2

  j = 0
  while j < len(l2):
    l3.append(l2[j])
    j= j + 2

if __name__ == '__main__':
   print('merge_list(l1,l2)')
   print(merge_list([1,2,3,4],[5,6,7,8]))


