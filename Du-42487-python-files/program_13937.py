def minimum(a):
   if len(a) == 1:
           return a[0]
   else:
           small = a[0]
           if a[1] < small:
                   small = a[i]
                   a.remove(a[0])
           else:
                   a.remove(a[1])
   return minimum(a)
