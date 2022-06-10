def reverse(a):
   rev = []
   i = 0
   while i < len(a):
      rev.append(a[len(a) - i])
      i = i + 1
   return rev
