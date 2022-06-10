def swap(a, i , j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def reverse(a):
   i = 0
   while i < len(a)/2:
      j = len(a) - 1 - i
      swap (a, i, j)
      i = i + 1