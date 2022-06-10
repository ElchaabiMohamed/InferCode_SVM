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
   j = 1
   p = 0
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   return p
