def maximum(l, i = 0):
	j = i
	while j < len(l) and l[j] > l[-1]:
		j += 1
	if j < len(l):
		tmp = l[i]
		l[i] = l[j]
		l[j] = tmp
	if j > len(l):
		return l[-1]
	return maximum(l, i + 1)
