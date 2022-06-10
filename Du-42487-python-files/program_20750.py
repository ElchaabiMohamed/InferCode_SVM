def union(a, b):
   c = set(a + b)
   return c

def intersection(a,b):
   c = []
   for item in a:
      if item in b:
         c.append(item)
   return set(c)



