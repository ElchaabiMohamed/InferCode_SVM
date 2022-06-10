#!/bin/usr/env python

def bsearch(a,q):
   low = 0
   high = len(a)
   while high != low:
      search = (high + low)/2
      if a[search] == q and a[search-1] != q:
         return search
      elif a[search] > q:
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
