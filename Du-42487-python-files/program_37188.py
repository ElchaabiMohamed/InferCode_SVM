#!/usr/bin/env python

def find_smallest_position(a,i):
   p = i
   j = i + 1
   while j < len(a):
      if a[i] < a[p]:
         p = j
      j = j + 1
   return p

def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def selection_sort(a):
   i = 0
   while i < len(a):
      p = find_smallest_position(a, i)
      swap(a,i,j)
      i = i + 1
