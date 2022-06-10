#!/bin/usr/env python
a = []
i = 0
j = 0
def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp
   return

def find_position_of_smallest(a,i):
   i = 0
   p = 0
   while i < len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1
   return p
