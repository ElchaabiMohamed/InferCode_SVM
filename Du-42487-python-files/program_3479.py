def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j] 
   a[j] = tmp
   
def find_position_of_smallest(a,i):
   p = i
   r = r + 1
   while r < len(a):
      if a[r] < a[p]:
         p = r
      r = r + 1
   return p
   
