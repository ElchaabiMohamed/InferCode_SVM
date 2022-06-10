import sys
a = sys.stdin.readlines()
seen = {}

def union(a,b):
   i = 0
   while i < len(a):
      if a[i] not in seen:        
         sys.stdout.write(a[i])
         seen[a[i]] = True
      i = i + 1   

def intersection(a,b):
   un = a + b
   return un
