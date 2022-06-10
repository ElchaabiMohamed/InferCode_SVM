
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

def intersection(a,b):
   int_seen = {}
   k = 0
   while k < len(a):
      if a[k] in b:
         int_seen[a[k]] = True
      k = k + 1


   return int_seen

if __name__ == "__main__":
   print(intersection([1, 2, 3], [2, 3, 4]))