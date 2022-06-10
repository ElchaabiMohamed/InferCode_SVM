
def power(m, n):
	if n == 0:
		return 1
	total = m**(n-2)
	return power(m, n-1) + (m**n)



