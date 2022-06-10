
def swap(a,i,j):
  tmp = a[j]
  a[j] = a[i]
  a[i] = tmp

def find_position_of_smallest(a,i):
  p = i
  while i < len(a):
    if a[i] < a[p]:
      p = i
    i = i + 1
  return p

def sort(a):
  i = 0
  while i < len(a):
    p = find_position_of_smallest(a,i)
    swap(a,i,p)
    i = i + 1


