
# a = [0,1,2,3,4]

# swap(a,0,1)

def swap(a,i,j):
 tmp = a[i]
 a[i] = a[j]
 a[j] = tmp


# a = [0,1,2,3]
# find(a,0)

def find_position_of_smallest(a,i):
 p = 0
 i = 1
 while i < len(a):
  if a[i] < a[p]:
   p = i
 i = i + 1



  
   
  
 
   
