#!/bin/usr/env python

def selection_sort(a):

   i = 0
   while i < len(a):

      p = i

      j = p + 1
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j = j + 1

      a_tmp = a[p]
      a[p] = a[i]
      a[i] = a_tmp

      i = i + 1


   z = 0 
   while z < len(a):
      print(a[z])
      z = z + 1












