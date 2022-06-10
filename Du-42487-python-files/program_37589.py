
def power(m, n):
	if n == 0:
		return 1
	if m == 0:
		return 0
	total = m**(n-2)
	return power(m, n-1) + (m**n)



