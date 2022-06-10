#!/usr/bin/env python

def selection_sort(a):
   
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
         if int(a[j]) < int(a[p]):
            p = j
         j = j + 1
    
      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp
      
      i = i + 1 
   return a
