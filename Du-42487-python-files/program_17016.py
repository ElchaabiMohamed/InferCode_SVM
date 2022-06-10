
def maximum(n):
	m = sorted(n)
	if n[0] == m[len(n)-1]:
		return n[0]
	return m[len(n)-1]