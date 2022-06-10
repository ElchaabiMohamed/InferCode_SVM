

def swap(a,i,j):
  tmp = a[j]
  a[j] = a[i]
  a[i] = tmp

def find_position_of_smallest(a,i):
  p = i
  while i < len(a):
    if a[j] < a[i]:
      j = i
    i = i + 1
  return i
