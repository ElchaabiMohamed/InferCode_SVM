import sys
a = sys.stdin.readlines()
seena = {}
b = sys.stdin.readlines()
seenb = {}

def union(a,b):
   i = 0
   while i < len(a+b):
      if a[i] not in seena:        
         sys.stdout.write(a[i])
         seen[a[i]] = True
      elif b[i] not in seenb:
         sys.stdout.wrtie(b[i])
         seen[b[i]] = True
      i = i + 1   

def intersection(a,b):
   un = a + b
   return un
