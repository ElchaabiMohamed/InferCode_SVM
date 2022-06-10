def bsearch(arr, tgt):
    lo = 0
    hi = len(arr)
    while lo <= hi and (lo + hi) / 2 < len(arr):
        mid = (lo + hi) / 2
        if arr[mid] < tgt:
            lo = mid + 1
        else:
            hi = mid - 1
    return (lo + hi) / 2