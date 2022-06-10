

def swap(a,i,j):
  tmp = a[j]
  a[j] = a[i]
  a[i] = tmp

def find_position_of_smallest(a,i):
  i = 0
  j = 1
  while i < len(a):
    if a[j] < a[i]:
      j = i
    i = i + 1
