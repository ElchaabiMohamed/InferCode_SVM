def swap(a, i , j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   n = len(a)
   i = 0
   p = 0
   while i < n:
      if a[i] < a[p]:
         p = i
      i = i + 1
