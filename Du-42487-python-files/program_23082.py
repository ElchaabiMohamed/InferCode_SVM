#!usr/bin/env python

import sys

def bsearch(a,q):
   low = 0
   high = len(a)

   while low < high:
      mid = (low + high) / 2
      
      if a[mid] < q:
         low = mid + 1
      else:
         high = mid
   return low

def contains(a,q):
   p = bsearch(a,q)
   return p < len(a) and a[p] == q