def partition(A, p, r):	#p is first, r is last

	q = j = p

	while j < r:

		if A[j] <= A[r]:
			A[q], A[j] = A[j], A[q]
			q += 1
		j += 1

	A[q], A[r] = A[r], A[q]

	return q

def quicksort(A, p, r):

	if r <= p:
		return

	q = partition(A, p, r)
	quicksort(A, p, q-1)
	quicksort(A, p+1, r)