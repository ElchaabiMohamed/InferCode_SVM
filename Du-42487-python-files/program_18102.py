def minimum(a):
   m = a[0]
   for n in a:
      if n < m:
         m = n
   return(m)
