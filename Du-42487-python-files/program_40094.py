def union(a, b):
	i = 0
	seen = []
	while i < len(a) :	
		seen[a[i]] = True 
		i = i + 1

	k = 0
	while k < len(b):	
		if not (b[k] in seen):
			seen[b[k]] = True
		k = k + 1

	return seen			