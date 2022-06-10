
def bsearch(a,q):
   low = 0
   high = len(a)

   while low < high:
      mid = (low + high) / 2
      assert low <= mid < high

      if a[mid] < q:
         low = mid + 1
         assert a[low - 1] < q or low == 0
      else:
         high = mid
         assert q <= a[high] or high == len(a)

   return low

