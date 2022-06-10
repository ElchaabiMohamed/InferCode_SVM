def union(a, b):
   un = {}

   i = 0
   while i < len(a):
      un[a[i]] = True 
      i = i + 1

   h = 0
   while i < len(b):
      un[b[h]] = True
      h = h + 1

   print(un)


def intersection(a, b):
   int = {}

   i = 0 
   while i < len(a):
      if a[i] in b and not (a[i] in int):
         int[a[i]] = True
      i = i +1

   print(int)


