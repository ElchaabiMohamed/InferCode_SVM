def power(m, n):
	if m ** n == 1:
		return 1
	if m ** n == 0:
		return 1
	return m ** power(m ** (n -1))