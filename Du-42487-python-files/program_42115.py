def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a, i):
   smallest = i
   while i < len(a):
      if a[i] < a[smallest]:
         smallest = i
      i = i + 1
   return smallest

def sort(a):
   i = 0
   while i < len(a):
      p = find_position_of_smallest(a, i)
      swap(a, i, p)
      i = i + 1
