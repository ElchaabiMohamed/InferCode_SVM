def bsearch(a, q):

    low = 0
    high = len(a)

    while low < high:
        mid = (low + high) / 2
        if a[mid] > q:
            high = mid

        elif a[mid] < q:
            low = mid + 1
            
        else:
            i = 0
            while i < len(a) and a[i] != q:
                i = i + 1
                return i
    return low