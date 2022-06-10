def bsearch(a, q):

    low = 0
    high = len(a)

    while low < high:
        mid = (low + high) / 2
        assert low <= mid < high

        if a[mid] > q:
            high = mid
            assert q <= a[high]

        else:
            low = mid + 1
            assert low == 0 or a[low - 1] < a

    return low