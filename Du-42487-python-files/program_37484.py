def union(a, b):
   i = ""
   c = []
   while i != "end":
       if a[i] not in c:
          c.append(a[i])
       elif c[i] not in c:
          c.append(c[i])
       else:
          i = "end"
   return c


