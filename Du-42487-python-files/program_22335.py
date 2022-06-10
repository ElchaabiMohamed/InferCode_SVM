a=[]
i=0
j=0

def swap(a,i,j):
   tmp = a[j]
   a[i] = a[j]
   a[i] = tmp

def find_position_of_smallest(a,i):
   x = i
   
   while i < len(a):
      if a[i] < a[x]:
         x = i
      i = i + 1
   return x
   
