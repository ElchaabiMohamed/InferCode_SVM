def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    tmp = a[j]
def func_reverse(a):
   i = 0
   while i < len(a):
       j = len(a) - 1 - i
       swap(a,i,j)
       i = i + 1
