#!/usr/bin/env python

def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   p = i
   i = i + 1
   while i < len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1

if __name__ == "__main__":
   a = [0,1,2,3]
   swap(a,1,3)
   print(a)
