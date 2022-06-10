def minimum(n, i=0):
	j = i

	while j<len(n) and n[j] > n[-1]:
		j += 1

	if j < len(n):
		tmp = n[i]
		n[i] = n[j]
		n[j] = tmp

	if j > len(n):
		return n[0]

	return minimum(n, i+1)
