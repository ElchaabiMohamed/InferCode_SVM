def bsearch(a,q):
    low = 0
    high = len(a)
    
    while low < high:
        mid = len(a) / 2
        assert low <= mid < high
        
        if a[mid] < q:
            low = mid + 1
            assert a[low - 1] < q
            
        else:
            high = mid
            assert q < a[high + 1]
            
        return low
            
        
























#def bsearch(a,q):
#    low = 0
#    high = len(a)
    
#    while low < high:
 #       mid = (low + high) / 2
#        assert low <= mid < high
        
 #       if a[mid] < q:
  #          low = mid + 1
   #         assert a[low-1] < q
 #       else:
  #          high = mid
#            assert q <= a[high]
            
   # return low