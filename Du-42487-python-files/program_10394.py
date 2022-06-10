def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp
  
def find_position_of_smallest(a,i):
   p = i
   while i < len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1
   return p

def sort(a):
  find_position_of_smallest(a,i)
  swap(a,i,j)
  
