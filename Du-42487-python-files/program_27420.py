def swap(a, i , j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,j):
   p = 0
   j = 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
