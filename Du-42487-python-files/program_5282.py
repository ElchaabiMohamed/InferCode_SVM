def bsearch(a, q):
    low = 0
    high = len(a) - 1

    mid = 0
    while low < len(a) and a[low] < q:
        mid = (high + low) // 2
        if a[mid] < q:
            low = mid + 1
        else:
            high = mid
    return low