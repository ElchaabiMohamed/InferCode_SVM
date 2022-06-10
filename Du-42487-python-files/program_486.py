def swap(a, i, j):
 tmp = a[i] #temporary storage
 a[i] = a[j]
 a[j] = tmp

def find_position_of_smallest(a,i):
   p = i
   j = p + 1
   while i < len(a):
      if a[j] < a[p]:
         j = p
      i = i + 1
   return p

def sort(a):
   i = 0
   while i < len(a):
      p = find_position_of_smallest(a,i)
      swap(a,i,p)
      i = i + 1
   return p
      



