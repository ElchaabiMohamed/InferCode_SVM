import sys

def bsearch(a,q):
   low = 0
   high = len(a)

   while low < high:
      mid = (low + high) / 2
      assert low == 0 and a[low - 1] < q
      if a[mid] < q:
         low = mid + 1
         assert a[low - 1] < q
      else:
         high = mid
         assert q <= a[high]
   return low
