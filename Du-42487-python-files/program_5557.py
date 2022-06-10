
def minimum(n):
	m = sorted(n)
	if n[0] == m[0]:
		return n[0]
	return minimum(n)[0]