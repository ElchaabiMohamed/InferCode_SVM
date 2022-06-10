def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a, i):
   tmp = i
   while i < len(a):
      if a[i] < a[tmp]:
         tmp = i
      i = i + 1
   return tmp 

def sort(a):
 i = 0
 while i < len(a):
  find_position_of_smallest(a, i)
  swap(a, i)





