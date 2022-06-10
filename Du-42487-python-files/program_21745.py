def selectionsort(A):
  i = 0
  while i < len(A):
    p = i
    j = i + 1
    while j < len(A):
      if A[j] > A[i]:
        p = j
      j = j + 1

    tmp = A[p]
    A[p] = A[i]
    A[i] = tmp
    i = i + 1
