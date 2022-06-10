d={}

import sys


def union(a,b):
   x = a + b
   while 0 < len(x):
      i = 0
      while i < len(x) and x[i] != x:  
         i = i + 1
   if i == len(x):
      d[x[i]] = True

      
   

#if __name__ == "__main__":
   print(union([1,2,3],[3,4,5]))
   

