def bsearch(a,q):
    high=len(a)
    low=0
    while low<high:
        mid=(low+high)/2
        if a[mid]<p:
            low=mid+1
        else:
            high=mid
    return low   