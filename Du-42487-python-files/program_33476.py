def union(a, b):
   i = 0
   c = []
   while i < len(a):
       if b[i] not in c:
          c.append(b[i])
       elif a[i] not in c:
          c.append(a[i])
       i = i + 1
   return c
