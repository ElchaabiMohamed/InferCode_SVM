def minimum(m = []):
	i = 0
	a = m[i]
	while i < len(m):
		if a < m[i]:
			a = m[i]
		i += 1
	return a