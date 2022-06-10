a = [4, 3, 2, 1]

def swap(a, i, j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp

def reverse(a):
    i = 0
    while i < len(a):
        tmp = a[len(a) - i]
        a[len(a) - i] = a[i]
        a[i] = tmp
        i = i + 1


