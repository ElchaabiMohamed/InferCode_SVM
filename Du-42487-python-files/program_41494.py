def swap (a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a

def reverse(a):
    k = 0
    while k < len(a)/2:
        swap(a, k, len(a) - k - 1)
        k += 1
