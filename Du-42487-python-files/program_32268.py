# recursively partition list until sorted
def quicksort(A, p, r):

    # return if nothing to sort (zero or one element)
    if r <= p:
        return

    # partition and sort left and right sublists
    q = partition(A, p, r)
    quicksort(A, p, q-1)
    quicksort(A, q+1, r)
