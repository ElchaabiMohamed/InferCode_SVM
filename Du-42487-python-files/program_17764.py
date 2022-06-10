def maximum(a):
   if len(a) == 1:
           return a[0]
   else:
           large = a[0]
           if a[1] > a[0]:
                   a.remove(a[0])
           else:
                   a.remove(a[1])
   return maximum(a)
