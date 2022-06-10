def union(a, b):
   c = []
   for item in a:
         if item not in c:
            c.append(item)
  
   for item in b:
      if item not in c:
         c.append(item)
   return c




def intersection(a,b):
   c = []
   for item in a:
      if item in b and item not in c:
          c.append(item)
   return c
   


print(intersection([1,2,3,4],[4,5,6,7]))
