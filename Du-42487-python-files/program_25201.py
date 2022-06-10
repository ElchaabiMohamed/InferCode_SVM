a = [6, 5, 4, 3, 2, 1]

def swap(a, i, j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp
    return a


def reverse(a):
    i = 0
    while i < len(a):
        j = len(a) - i - 1
        tmp = a[j]
        a[j] = a[i]
        a[i] = tmp
        i = i + 1
    return a

reverse(a)
print(a)






