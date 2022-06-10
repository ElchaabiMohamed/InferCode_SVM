def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def reverse(a):
    for i in range(0,len(a)/2):
        swap(a, i, len(a)-i -1)