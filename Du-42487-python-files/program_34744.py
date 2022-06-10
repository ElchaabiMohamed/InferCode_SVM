def maximum(a):
   try:
      if a[0] > a[1]:
         return maximum(a[:1] + a[2:])
      else:
         return maximum(a[1:])
   except IndexError:
      return a[0]
