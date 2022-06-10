def partition(A, p, r):
	#q and j start at p
	q = j = p

	while j < r:
		if A[j] <= A[r]:
			A[q], A[j] = A[j], A[q]
			q += 1
		j += 1

	A[q], A[r] = A[r], A[q]

	return q