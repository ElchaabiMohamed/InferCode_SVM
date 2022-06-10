def partition(A, p, r):

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
		return A[0]

	q = partition(A, p, r)
	quicksort(A, p, q-1)
	quicksort(A, q+1, r)

def minimum(l):
	A = l
	p = 0
	r = len(A) - 1

	return quicksort(A, p, r)