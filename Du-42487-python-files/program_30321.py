def swap(a, i, j):
   tmp = a[i]
   a[i]= a[j]
   a[j]= tmp

def find_position_ofsmallest(a, i):
   j = i
   while i < len(a):
      if a[i] < a[j]:
         j = i
      i = i + 1
   return j

def sort(a):
   i = 0
   while i < len(a):
      k = find_position_of_smallest(a, i)
      swap( a, i, k)
      i = i + 1
