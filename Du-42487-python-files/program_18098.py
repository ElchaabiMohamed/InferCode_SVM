def swap(a, i, j):
   tmp  = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a, i):
 x = 0  
 while x < len(a):
   n = x
   j = i + 1
   while j < len(a):
      if a[j]  < a[n]:
          n = j
      j = j + 1	
   
         
    
