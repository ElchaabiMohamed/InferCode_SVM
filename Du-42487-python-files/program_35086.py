import sys
a = sys.stdin.readlines()
seena = {}
b = sys.stdin.readlines()
seenb = {}
c = []
def union(a,b):
   i = 0
   while i < len(a+b):
      if a[i] not in seena:        
         c.append(a[i])   
      elif b[i] not in seenb:
         c.append(a[i])   
      i = i + 1   
   print(c)
def intersection(a,b):
   un = a + b
   return un
