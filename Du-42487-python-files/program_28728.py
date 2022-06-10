def minimum(a):
   try:
      if a[0] < a[1]:
         return minimum(a[:1] + a[2:])
      else:
         return minimum(a[1:])
   except IndexError:
      return a[0]
