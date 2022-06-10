i = 0
def selection_sort(a):
    while i < len(a):
      j = i
      k = i
      while k < len(a):
          if a[j] > a[k]:
              k = j
          k = k + 1

      swap(a,i,j)
      
      i = i + 1