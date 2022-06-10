#!/usr/bin/env python

def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   i = 0
   while i < (len(a) - 1):
      j = i + 1
      swap(a,i,j)
      i += 1
   return a
