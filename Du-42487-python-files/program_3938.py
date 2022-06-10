def union(a, b):
   s = a + b
   return set(s)

def intersection(a, b):
   i = 0
   s = []
   while i < len(a) and i < len(b):
      if a[i] in b:
         s.append(a[i])
      i = i + 1
   return s
   n = 0
   x = []
   while n < len(s):
      if s[n] not in s:
         x.append(s[n])
      n = n + 1
   return x
