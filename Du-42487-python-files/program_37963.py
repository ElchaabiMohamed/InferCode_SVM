
def selection_sort(a,j,k):
    while i < len(a):
      j = i
      k = i
      while k < len(a):
          if a[j] > a[k]:
              k = j
          k = k + 1

      swap(a,i,j)
      
      i = i + 1