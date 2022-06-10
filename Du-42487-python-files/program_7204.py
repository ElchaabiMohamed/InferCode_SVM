def selectionsort(A):
	for h in range (len(A)):
		min_i = h
		for i in range(h, len(A)):
			if A[i] < A[min_i]:
				min_i = i
		A[h], A[min_i] = A[min_i], A[h]
