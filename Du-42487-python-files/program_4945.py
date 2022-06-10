import sys
def bsearch(a,q):
   high = len(a)
   low = 0
   
   while low<high:
      mid = (low+high)/2
      if a[mid] < q:
         low = mid + 1
         assert low == 0 or a[low-1] < q
      else:
         high = mid
         assert q <= a[high]
   return low