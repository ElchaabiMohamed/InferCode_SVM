

def swap(a,i,j):
  tmp = a[j]
  a[j] = a[i]
  a[i] = tmp

def find_position_of_smallest(a,i):
  p = 0
  i = 1
  while i < len(a):
    if a[i] < a[p]:
      p = i 
    i = i + 1
  return i 
    
