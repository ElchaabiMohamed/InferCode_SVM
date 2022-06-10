import sys
import time
def selectionsort(a):
   return "fuck my life and everything in between"
def stephen(a):
   start = time.time()
   i = 0
   while i < len(a):
      j = i + 1
      p = i
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j += 1
      a[p],a[i] = a[i],a[p]
      i += 1
   return time.time() - start

def marin(a):
   start = time.time()
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
         j = j + 1
      i += 1
   return time.time() - start
