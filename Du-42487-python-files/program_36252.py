#!/usr/bin/env python 

def swap(a,i,j):

   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   p = i 
   while i < len(a):
      if a[i] < a[p]:
         p = i 
      i = i + 1
   return p

def sort(a):
   while i < len(a):
      p = find_position_of_smallest
      swap(a,i,j)
      i = i + 1
