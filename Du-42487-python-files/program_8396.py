def swap(a,i,j):
 
   temp = a[i]
   a[i] = a[j]
   a[j] = temp 

def find_position_of_smallest(a,i):
   i = 0
   p = i
   while i < len(a):
      if a[i] > a[p]:
         i = i + 1        
   return a     

