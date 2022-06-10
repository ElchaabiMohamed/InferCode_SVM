def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp 

def find_position_of_smallest(a,i): 
   tmp = i  
   while i < len(a):
      if a[i] < a[tmp]:
         tmp = i 
      i = i + 1 
   return tmp  

def sort(a):
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1
