import sys

def bsearch(a,q):
   low = 0
   high = len(a)


   while low < high:
      mid = (low + high)/2
      assert low <= mid < high


      if a[mid] < q:
         low = mid + 1
         assert low == 0 or a[low-1] < q
      else:
         high = mid 
         assert q <= a[high]
   return low
   
#if __name__ == "__main__":
  #bsearch([2,3,6,6,7,8], 1)  
 # bsearch([2,3,6,6,7,8], 2)  
 # bsearch([2,3,6,6,7,8], 6)  
 # bsearch([2,3,6,6,7,8], 8)  
 # bsearch([2,3,6,6,7,8], 9)  
 # bsearch([2,3,6,6,7,8], 4)  


