def swap(a,i,j):
   a[tmp] = a[i]
   a[i] = a[j]
   a[j] = a[tmp]

def reverse(a):
   i=0
   while i<len(a)/2:
      a[tmp] = a[i]
      a[i] = a[len(a)-i-1]
      a[len(a)-i-1] = a[tmp]
      i=i+1
