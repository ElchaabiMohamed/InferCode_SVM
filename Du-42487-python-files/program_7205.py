a = []
def swap(a,i,j):
  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

def find_position_of_smallest(a,i):
  
  p = a[i]
  j = i + 1
  while i < len(a):
    if a[j] < p:
      p = a[j]
    return p
  i = i + 1
