a = []
def swap(a,i,j):
  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

def find_position_of_smallest(a,i):
  
  p = a[i]
  i = 0
  while i < len(a[i]):
    if a[i] < p:
      p = a[i]
    return a[i]
  i = i + 1
