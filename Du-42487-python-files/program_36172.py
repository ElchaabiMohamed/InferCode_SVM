#!/usr/bin/env python

a = []
q = 0

def bsearch(a,q):
   low = 0
   high = len(a)
   while low < high:
      mid = (high + low)/2
      if a[mid] < q:
         assert low == 0 or a[low-1] < q
         assert high == len(a) or q <= a[high]
      else:
         mid = low
         


