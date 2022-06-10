def swap(a,i,j):
   y = a[j]
   a[j] = a[i]
   a[i] = y
   


def reverse(a):
   i = 0
   while i < len(a)/2:
      swap(a,i,len(a)-i-1)
      i = i + 1
