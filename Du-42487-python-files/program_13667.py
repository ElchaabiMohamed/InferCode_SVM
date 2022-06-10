a = []
def swap(a,j,i):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a
def reverse(a):
    i = len(a)-1
    j = 0
    while i != 0 and j < len(a) and j != i:
       swap(a,i,j) 
       i = i - 1
       j = j + 1
    return a

