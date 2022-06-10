def swap(a,i,j):
 tmp = a[i]
 a[i] = a[j]
 a[j] = tmp

def find_position_of_smallest(a,i):
 s = i 
 while i < len(a):
  if a[i] < a[s]:
   s = i
  i = i + 1
 return s

def sort(a):
 i = 0
 while i < len(a):
  x = find_position_of_smallest(a,i)
  swap(a,i,x)
 return x


