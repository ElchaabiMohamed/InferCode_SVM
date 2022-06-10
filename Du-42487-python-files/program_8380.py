def quicksort(cabbages):
    if len(l) < 2:
        return l
    pivot = l[0]
    left_side = []
    right_side = []
    for n in cabbages[1:]:
        if n < pivot:
            left_side.append(n)
        else:
            right_side.append(n)
    return quicksort(left_side) + [pivot] + quicksort(right_side)