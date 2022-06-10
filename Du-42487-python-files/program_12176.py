def maximum(n):
	if len(n) == 1:
		return n[0]
	if n[0] > n[1]:
		n.remove(n[1])
	else:
		n.remove(n[0])

	return maximum(n)