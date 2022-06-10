import sys
a = sys.stdin.readlines()
seen = {}

def union(a,b):
   i = 0
   while i < len(lines):
      if lines[i] not in seen:        
         sys.stdout.write(lines[i])
         seen[lines[i]] = True
      i = i + 1   

def intersection(a,b):
   un = a + b
   return un
