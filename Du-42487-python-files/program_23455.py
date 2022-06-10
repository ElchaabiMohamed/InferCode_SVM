def reverse(a):
   i = 0
   j = len(a)
   while i < len(a):
      tmp = a[i]
      a[i] = a[j-i]
      a[j-i] = tmp
      i = i + 1
   print(a) 
