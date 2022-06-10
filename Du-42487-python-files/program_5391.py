def swap(a,i,j):
   a[tmp] = a[i]
   a[i] = a[j]
   a[j] = a[tmp]

def reverse(a):
   i=0
   while i<len(a)/2:
      swap(a, i, len(a)-i-1)
      i=i+1
