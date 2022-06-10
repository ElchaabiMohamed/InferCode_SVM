def swap(a, i, j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp
    return a


def reverse(a):
    i = 0
    while i < len(a)/2:
        j = len(a) - i - 1
        tmp = a[j]
        a[j] = a[i]
        a[i] = tmp
        i = i + 1
    return a








