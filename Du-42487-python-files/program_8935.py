#!/usr/bin/env python

a = [0, 1, 2, 3, 4, 5]

def swap(a,i,j):
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp

def reverse(a):
   i = 0
   j = len(a) + 1
   while i < len(a):
      swap(a,i,j)
      i = i + 1
      j = j - 1
