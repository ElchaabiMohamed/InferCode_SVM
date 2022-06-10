#!/bin/usr/env python

def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def reverse(a):
   i = 0
   j = len(a) - 1
   while i < len(a)/2:
      swap(a,i,j)
      i += 1
      j -= 1

def main():
   a = [4,3,1,2]
   swap(a,2,3)
   print(a)
   reverse(a)
   print(a)

if __name__ == "__main__":
   main()
