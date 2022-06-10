a = []

def swap(a,i,j):
  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

def find_position_of_smallest(a,i):
   p = i
   j = i + 1
   while i < len(a):
      a[p] <a[j]
   j = j + 1
   return p
