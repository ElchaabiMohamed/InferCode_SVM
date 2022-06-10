def union(a,b):
   c = {}

   i = 0
   while i <len(a):
      c[a[i]] = True
   i = i + 1

   k = 0
   while k <len(b):
      if not (b[k] in c):
         c[b[k]] = True
      k = k + 1
   
   return c

def intersection(a,b):
   c = {}

   i = 0
   while i <len(a):
      if a[i]in b and not (a[i] in c):
         c[a[i]] = True
      i = i + 1
   
   return c
