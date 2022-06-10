#!/usr/bin/env python3

import random

def quicksort(l, first, last):
    if first >= last:
        return
    i, j = first, last
    pivot = l[random.randint(first, last)]

    while i <= j:
        while l[i] < pivot:
            i += 1
        while l[j] > pivot:
            j -= 1
        if i <= j:
            l[i], l[j] = l[j], l[i]
            i, j = i + 1, j - 1

    quicksort(l, first, j)
    quicksort(l, i, last)
    return l
