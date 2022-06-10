def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def smallest_position(a):
   smallest=0
   j=1
   while j<len(a):
      if a[j]<a[smallest]:
         smallest=j
      j=j+1
   return smallest

def selection_sort(a):
   i=0
   while i<len(a):
      p = smallest_position(a[i:])
      swap(a,i,p)
      i=i+1
