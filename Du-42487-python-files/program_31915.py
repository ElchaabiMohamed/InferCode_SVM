def union(a, b):
   c = set(a + b)
   return c

def intersection(a,b):
   c = []
   for item in a:
      if item in b:
         c.append(item)
   return set(c)


print(intersection([1,2,3,4,5],[3,5,6,7,8,4]))
