def swap (a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   p = i
   j = i + 1
   while i < len(a):
      if a[i] < a[j]:
         p = i
      i = i + 1
   return p

