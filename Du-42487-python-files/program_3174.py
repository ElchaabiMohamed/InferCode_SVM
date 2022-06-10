#!/usr/bin/env python
a = []
q = 0
i = 0


while i < len(a):
   a[i] = int(a[i])
   i = i + 1

def bsearch(a,q):
   low = 0
   high = len(a)

   while low != high:
      m = (low + high)/2
      if a[m] < q:
         low = m + 1
      else:
         high = m
   return low
