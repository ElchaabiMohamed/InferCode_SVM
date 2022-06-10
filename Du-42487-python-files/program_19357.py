def maximum(a):
   if len(a) == 1:
      return a[0]
   else:
      nl = maximum(a[1:])
   if a[0] > nl:
      return a[0]
   else:
      return nl

