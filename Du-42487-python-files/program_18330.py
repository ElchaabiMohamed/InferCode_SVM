#!/bin/usr/env python

def bsearch(a,q):
   low = 0
   high = len(a)
   search = (high + low)/2
   while high != low and a[search] != q:
      search = (high + low)/2
      if a[search] > q:
         high = search
      else:
         low = search
         if low == search:
            low += 1
   return search

def main():
   print(bsearch([1,2,3,4,5],4))
   print(bsearch([1,2,3,4,5],0))

if __name__ == "__main__":
   main()
