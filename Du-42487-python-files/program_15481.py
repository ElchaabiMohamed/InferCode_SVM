def bsearch(a, q):
    a = sorted(a)
    low = 0
    high = len(a)

    while low < high:
        mid = (low + high) / 2
        if a[mid] > q:
            high = mid
        else:
            low = mid + 1

    return low