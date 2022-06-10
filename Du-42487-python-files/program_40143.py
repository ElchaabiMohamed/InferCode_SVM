a = []

def swap(a,i,j):
  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

def find_position_of_smallest(a,i):
   p = i
   x = i + 1
   while i < len(a):
      p = x
   i = i + 1
