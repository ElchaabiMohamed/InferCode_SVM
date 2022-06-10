def bsearch(a, q):
    low = 0
    high = len(a)
    
    while low < high:
        mid = (low + high) / 2
        assert low <= mid < high
        
        if q < mid:
            low = mid
            assert a[low-1] < q
            
        else:
            high = mid
            assert q <= a[high]
            
    return low
            