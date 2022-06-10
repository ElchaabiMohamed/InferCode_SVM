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
   n = 0
   prev = s[n]
   curr = s[n + 1]
   x = []
   while  (n - 1) < len(s):
      if curr != prev:
         x.append(prev)
      n = n + 1
   return x
