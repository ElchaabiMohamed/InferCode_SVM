def quicksort(l, start=0, end=None):
    if len(l) < 2:
        return l
    pivot = l[1]
    left = []
    right = []
    for n in l[1:]:
        if n < pivot:
            left.append(n)
        else:
            right.append(n)
    return quicksort(left) + [pivot] + quicksort(right)

print((quicksort([23,51,65,94,17,89,22,75])))
