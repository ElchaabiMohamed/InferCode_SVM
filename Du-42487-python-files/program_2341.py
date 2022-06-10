def selectionsort(A):
  for h in range(len(A)):
    mini = h
    for i in range(h,len(A)):
      if A[i] < A[mini]: 
        mini = i
    A[h], A[mini] = A[mini], A[h]
