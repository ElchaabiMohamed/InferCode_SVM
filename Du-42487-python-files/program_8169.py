def swap (a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   return p

def sort(p):
   
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1
