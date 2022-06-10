def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def smallest(a, i):
    minimum = i
    while i < len(a):
        if a[i] < a[minimum]:
            minimum = i
        i = i + 1
    return minimum


def selection_sort(a):
    i = 0
    while i < len(a):
        pos = smallest(a, i)
        swap(a, i, pos)
        i = i + 1
