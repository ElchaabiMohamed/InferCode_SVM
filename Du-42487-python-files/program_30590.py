a = []
i = 0
j = 0

def swap(a, i, j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def find_position_of_smallest(a, i):
   x = i

   while i < len(a):
      if a[j] < a[x]:
         x = j
      j = j + 1
   
   return x   