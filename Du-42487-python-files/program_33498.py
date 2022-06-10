def swap(a, i, j):
 tmp = a[i] #temporary storage
 a[i] = a[j]
 a[j] = tmp

def find_position_of_smallest(a,i):
 i = 0
 while i < len(a):
  if a[i] < a[j]:
   i = i + 1
  return i 

def sort(a):
   i = 0
   while i < len(a):
      p = find_position_of_smallest(a,i)
      swap(a,i,p)
      i = i + 1
   return p
      



