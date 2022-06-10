def reverse(a):
   i = 0
   rev = []
   while i < len(a):
      rev.append(a[len(a) - i - 1])
      i = i + 1
   return rev
