def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a, i):
   smallest = i
   while i < len(a):
      if a[i] < smallest:
         smallest = a[i]
      i = i + 1
   return smallest
