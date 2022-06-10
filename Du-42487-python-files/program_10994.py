def reverse_list(a):
   if not a:
      return a
   return str(a[-1]) + reverse_list(str(a[:-1]))
