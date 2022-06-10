seen = {}

def union(a,b):
	c = a + b
	union = []
	i = 0
	while i < len(c):
		if c[i] not in seen:
			seen[c[i]] = True
		i = i + 1

	for number in seen:
			union.append(number)

	return union


	
