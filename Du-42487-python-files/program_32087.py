a = []
def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a
def reverse(a):
    i = len(a)-1
    j = j + 1
    while i != 0 and j < len(a):
       swap(a,i,j) 
       i = i - 1
       j = j + 1
    return a
