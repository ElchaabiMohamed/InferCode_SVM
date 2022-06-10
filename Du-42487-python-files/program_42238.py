import sys 
def union(a,b):
   seen = {}            

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

def intersection(a,b):
   int_seen = {}
   
   f = 0
   while f < len(a):
      if a[f] in b:      
         int_seen[a[f]] = True
      f = f + 1

   return int_seen 



