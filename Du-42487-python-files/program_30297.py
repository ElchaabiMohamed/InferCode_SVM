def union(a, b):
   s = a + b
   return set(s)

def intersection(a, b):
   i = 0
   s = []
   while i < len(a) and i < len(b):
      if int(a[i]) in b:
         s.append(a[i])
      i = i + 1
   return s
