def QuickSort(A,p,r):

    if p<r:
        q=partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
    return A