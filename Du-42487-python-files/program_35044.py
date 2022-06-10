def union(a, b):
   i = 0
   c = {}
   while i < len(a):
       c.append(a[i])
       if b[i] not in c:
          c.append(b[i])
       i = i + 1
   return c
