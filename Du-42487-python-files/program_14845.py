a = []
def swap(a,j,i):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a
def reverse(a):
   
    i = 0
    while i< len(a)/2 :
       tmp = a[i]
       a[i] = a[len(a)-i-1]
       a[len(a)-i-1] = tmp
       i = i + 1
       
    return a

