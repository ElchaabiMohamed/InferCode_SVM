import sys

a = sys.stdin.readlines()
print(a)

def union(a, b):
   i = 0
   c = []
   while i < len(a):
       if a[i] not in c:
          c.append(a[i])
       elif c[i] not in c:
          c.append(c[i])
       i = i + 1
   return c


