def sumup(N):
	if N == 0:
		return 0
	else:
		return N + sumup(N-1)
