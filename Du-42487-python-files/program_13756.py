#!/usr/bin/env python

def swap(a, i ,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def reverse(a):
   i = 0
   while i < len(a)/2:
      swap(i , len(a)-i-1)
      i = i + 1

if __name__ == "__swap__":
   swap()

if __name__ == "__reverse__":
   reverse()
