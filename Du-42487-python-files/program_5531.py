def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a, i):
   smallest = a[i]
   count = i
   while count < len(a):
      if a[i] <= smallest:
         smallest = a[i]
      count = count + 1
   return smallest
