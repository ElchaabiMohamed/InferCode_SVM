#!/bin/usr/env python

def bsearch(a,q):
   low = 0
   high = len(a)
   while low < high:
      search = (high + low)/2
      assert low <= search < high

      if a[search] < q:
         low = search + 1
         assert a[low-1] < q
      else:
         high = search
         assert q <= a[high]

   return low

def main():
   print(bsearch([1,2,3,4,5],4))
   print(bsearch([1,2,3,4,5],0))

if __name__ == "__main__":
   main()
