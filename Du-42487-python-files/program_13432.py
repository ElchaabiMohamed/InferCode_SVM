#!/usr/bin/env python

def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

if __name__ == "__main__":
   a = [0,1,2,3]
   swap(a,1,3)
   print(a)
