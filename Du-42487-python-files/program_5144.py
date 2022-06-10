def quicksort(A, p, r):

    if r <= p:
        return

    q = partition(A, p, r)
    quicksort(A, p, q-1)
    quicksort(A, q+1, r)
