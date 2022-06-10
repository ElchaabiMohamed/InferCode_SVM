def partition(A, p, r):
  q=j=p
  while j<r:
    if A[j]<=A[r]:
      A[q], A[j] = A[j], A[q]
      q+=1
    j+=1
  A[q], A[r] = A[r], A[q]
  return q

# recursively partition list until sorted
def quicksort(A, p, r):
    # return if nothing to sort (zero or one element)
    if r <= p:
        return

    # partition and sort left and right sublists
    q = partition(A, p, r)
    quicksort(A, p, q-1)
    quicksort(A, q+1, r)
