def swap(a, i, j):
   tmp  = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a, i):
 i = 0  
 while i < len(a):
   n = i
   j = i + 1
   while j < len(a):
      if a[j]  < a[n]:
          n = j
      j = j + 1	
   
         
    
