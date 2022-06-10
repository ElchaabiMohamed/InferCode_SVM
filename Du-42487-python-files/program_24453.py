#!/usr/bin/env python

def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def reverse(a):
   i = 0
   while i < len(a) / 2:
      swap(a,i,len(a)-i-1)
      i = i + 1

def main():
   a = [1, 2, 3, 4, 5, 6]
   swap(a,0,4)
   print(a)
   reverse(a)
   print(a)

if __name__ == "__main__":
   main()