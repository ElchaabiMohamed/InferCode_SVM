import sys
i = sys.stdin.readlines()

def union(a,b):
   c = a,b
   return c

def intersection(a,b):
   d = a + b
   return d

if __name__ == "__main__":
   print(sys.union(i))
   print(sys.intersection(i))

