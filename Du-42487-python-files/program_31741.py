def bsearch(a, q):
    low = 0
    high = len(a)
    
    while low < high:
        mid = (low + high) / 2
        if a[mid] < q:
            low  = mid + 1
        else:
            high = mid
    return low

if __name__ == "__main__":
    assert bsearch([2,3,6,6,7,8], 1) == 0
    assert bsearch([2,3,6,6,7,8], 2) == 0
    assert bsearch([2,3,6,6,7,8], 4) == 2
    assert bsearch([2,3,6,6,7,8], 6) == 2
    assert bsearch([2,3,6,6,7,8], 8) == 5
    assert bsearch([2,3,6,6,7,8], 9) == 6
