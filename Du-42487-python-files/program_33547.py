#!/usr/bin/env python

def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a, i):
   i = p
   p = i
   i = i + 1
   while i <len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1
   return p

def sort(a):
   i = 0
   while i < len(a):
      p = find_position_of_smallest(a, i)
      swap(a, i, p)
      i += 1

if __name__ == "__main__":
   import sys
   import random
   import time
