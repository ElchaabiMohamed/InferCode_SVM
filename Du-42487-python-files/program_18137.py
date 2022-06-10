def find_position_of_smallest(a,i):
   p = 0
   i = 0
   while i < len(a):
      if a[i] < a[p]:
         p = i 
      i = i + 1
   return p
