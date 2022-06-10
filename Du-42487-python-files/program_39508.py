seen = {}

def union(a,b):
	union = []
	i = 0
	while i < len(a) and i < len(b):
		if a[i] or b[i] not in seen:
			seen[a[i]] = True
			seen[b[i]] = True
		i = i + 1

	for number in seen:
			union.append(number)

	return union

	
	
