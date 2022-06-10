# Swap the elements at positions i and j in list a.

def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   i = 0
   while i < len((a) / 2):
      swap(a,i,len(a)-i -1)
   i = i + 1  
  

   




