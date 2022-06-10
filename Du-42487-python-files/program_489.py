
def union(a,b):
   seen = {}            # This is now a dictionary.

   i = 0
   while i < len(a):
      if a[i] not in seen:      
         seen[a[i]] = True
      i = i + 1

   j = 0
   while j < len(b):
      if b[j] not in seen:      
         seen[b[j]] = True
      j = j + 1


   return seen
