def bsearch(a, q):

    low = 0
    high = len(a)

    while low < high:
        mid = (low + high) / 2
        if a[mid] > q:
            high = mid
        else:
            low = mid + 1

    return low - 1