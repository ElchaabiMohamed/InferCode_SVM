#!/usr/bin/env python

import sys

def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp
   return a

def reverse(a):
   i = 0
   j = len(a) - 1
   while j < len(a) / 2:
      tmp = a[j]
      a[j] = a[i]
      a[i] = tmp
      i = i + 1
      j = j - 1
   return a

def main():
   print(swap(5,8,7))
   print(reverse([1,3,7,9]))

if __name__ == "__main__":
   main()
