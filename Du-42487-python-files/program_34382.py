def maximum(l):
	m = 0
	for line in l:
		if line > m:
			m = line
	return m