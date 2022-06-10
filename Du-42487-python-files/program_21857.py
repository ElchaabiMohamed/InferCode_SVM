#!/bin/usr/env python

def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   i = a[0]
   j = len(a)-1

   while i < j:
      a = swap(a)

      i = i + 1
      j = j - 1
