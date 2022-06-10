def swap (a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp 

def find_position_of_smallest(a,i):
   p = i
   i = i + 1
   while i < len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1
   return p

def sort(a):
   p = i + 1
   i = i + 2
   while i < len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1
   return p
