a =[]
def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a, i):
   p = i
   j = i + 1
   while j < len(a):
      if a[p] < a[j]:
         p = j  
      j = j + 1
   return p
