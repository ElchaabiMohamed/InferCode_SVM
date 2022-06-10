def bsearch(arr, tgt):
    lo = 0
    hi = len(arr)
    while lo != hi:
        mid = (lo + hi) / 2
        if arr[mid] < tgt:
            lo = mid + 1
        else:
            hi = mid - 1
    return (lo + hi) // 2 + 1 if arr[-1] == tgt else (lo + hi) // 2

