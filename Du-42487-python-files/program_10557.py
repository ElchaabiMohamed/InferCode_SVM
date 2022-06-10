
# a = [0,1,2,3,4]

# swap(a,0,1)

def swap(a,i,j):
 tmp = a[i]
 a[i] = a[j]
 a[j] = tmp


# a = [0,1,2,3]
# find(a,0)

def find_position_of_smallest(a,i):
  j = i
  while i < len(a):
   if a[i] < a[j]:
     j = i
   i = i + 1
  return j


def sort(a):
  i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1

   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1 



  
   
  
 
   
