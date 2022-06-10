i = 0
while i < len(a):
   a[i] = int(a[i])
   i = i + 1

def bsearch(a,q):
   low = 0
   high = len(a)

   while low < high:
      mid = (low + high)/2
      assert low <= mid < high

      if a[mid] < q:
         low = mid + 1
         assert a[low - 1] < a
      else:
         high = mid
         assert q <= a[high]

   return low
