def reverse(a,i,j):
   a = []
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

   return a