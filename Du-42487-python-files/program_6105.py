def swap(a, i , j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   n = len(a)
   j = 0
   p = 0
   while j < n:
      if a[j] < a[p]:
         p = j
      j = j + 1
