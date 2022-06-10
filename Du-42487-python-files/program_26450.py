#!usr/bin/env python

# function swaps position a[i] with a[j] in a list a.

def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

# reversers list a
def reverse(a):
   i = 0
   while i < len(a)/2:
      swap(a, i, len(a) - i - 1)
      i = i + 1