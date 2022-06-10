def swap(a, i, p):
   tmp = a[i]
   a[i] = a[p]
   a[p] = tmp
   
def findsmallest(a, i):
   p = i
   j = i + 1
   while j<len(a):
      if a[j]<a[p]:
         p=j
      j+=1
   return p

def selection_sort(a):
   i=0
   while i<len(a):
      p = findsmallest(a, i)
      swap(a, i, p)
      i+=1
   return a