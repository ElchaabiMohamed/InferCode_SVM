def minimum(l):
   if len(l) == 1:
      return l[0]

   if l[0] < l[1]:
      l.remove(l[1])
   elif l[0] > l[1]:
      l.remove(l[0])

   return minimum(l)