def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def quicksort(l, p, r):
    if r <= p:
        return l
    q = p
    for j in range(p, r):
        if l[j] <= l[r]:
            swap(l, j, q)
            q += 1
    swap(l, q, r)
    quicksort(l, p, q - 1)
    quicksort(l, q + 1, r)
    return l
