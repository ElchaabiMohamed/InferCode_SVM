def bsearch(a, q):
    lo = 0
    hi = len(a)

    while lo < hi:
        mid = (lo + hi) / 2
        if a[mid] < q:
            lo = mid + 1
        else:
            hi = mid
    
    return lo