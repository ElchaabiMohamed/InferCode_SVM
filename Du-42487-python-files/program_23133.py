import sys

def union(a,b):
  i = 0 
  d = {}
  while i < len(a):
    d[a[i]] = True 
    i = i + 1
    print(d) 

if __name__ == "__main__":
  print(union([1,2,3],[3,4,5]))

