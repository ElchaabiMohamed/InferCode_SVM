

def swap(a,i,j):
  tmp = a[j]
  a[j] = a[i]
  a[i] = tmp

def find_position_of_smallest(a,i):
  j = 0
  i = 1
  while i < len(a):
    if a[i] < a[j]:
      j = i
    i = i + 1
