def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   i = 0
   p = 1
   while i < len(a):
      if a[i] < a[p]:
         p = i 
      i = i + 1
   return p
