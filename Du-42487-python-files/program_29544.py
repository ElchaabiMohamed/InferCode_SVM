def union(a, b):
   un = {}

   i = 0
   while i < len(a):
      un[a[i]] = True 
      i = i + 1

   j = 0
   while i < len(b):
      if not (b[j] in un):
         un[b[j]] = True
      j = j + 1

   return un


def intersection(a, b):
   inter = {}

   i = 0 
   while i < len(a):
      if a[i] in b and not (a[i] in inter):
         inter[a[i]] = True
      i = i +1

   return inter


