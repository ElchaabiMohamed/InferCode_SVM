def quicksort(l, p, r):
    if r <= p:
        return
    q = j = p
    while j < r:
        if l[j] <= l[r]:
            l[q], l[j] = l[j], l[q]
            q += 1
        j += 1
    l[q], l[r] = l[r], l[q]
    quicksort(l, p, q-1)
    quicksort(l, q+1, r)
