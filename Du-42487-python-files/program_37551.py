
def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a, i):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j  
      j = j + 1
   return p

def sort(a):
   i = 0
   j = i + 1
   while i < len(a):
      find_position_of_smallest(a, i)
      swap(a, i, j)
   j = i
   i = i + 1
