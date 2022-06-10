#!/usr/bin/env python

def swap(a, i, j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def reverse(a):
   i = 0
   j = -1
   while i < len(a)/2:
      swap(a, i, j)
      i += 1
      j -= 1