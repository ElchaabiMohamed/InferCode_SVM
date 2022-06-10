def partition(a, p, r):
    q = j = p
    while j < r:
        if a[j] < a[r]:
            a[q], a[j] = a[j], a[q]
            q += 1
        j += 1

    a[q], a[r] = a[r], a[q]
    return q


def quicksort(A, p, r):

    if r <= p:
        return

    q = partition(A, p, r)
    quicksort(A, p, q-1)
    quicksort(A, q+1, r)
