import sys
a = sys.stdin.readlines()
b = sys.stdin.readlines()
import sys

def union(a,b):
   i = 0
   while i < len(a) and a[i] != b:
      i = i + 1

   return i < len(a)

i = 0
while i < len(a + b):
   if not is_in(seen, a[i]):    # <-- We use the "is_in" function.
      sys.stdout.write(a[i])
      seen.append(a[i])
   i = i + 1

def intersection(a,b):
   un = a + b
   return un
