def reverse(a):
   i = 0
   while i < len(a):
      tmp = a[i]
      a[i] = a[len(a)-i]
      a[len(a)-i] = tmp
      i = i + 1
   print(a) 
