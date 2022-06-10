def quicksort(l):
    if len(l) < 2:
        return l
    pivot = l[0]
    left = []
    right = []
    for n in l[1:]:
        if n < pivot:
            left.append(n)
        else:
            right.append(n)
    return quicksort(left) + [pivot] + quicksort(right)