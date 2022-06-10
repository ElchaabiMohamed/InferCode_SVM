def union(a, b):
	a = a + b
	seen = {}
	c = []
	
	i = 0 
	while i < len(a):
		if a[i] not in seen:
			seen[a[i]] = True
		i = i + 1

	for number in seen:
		c.append(number)

	return c

def intersection(a,b):
	seen = {}
	append = {}
	c = []

	i = 0 
	while i < len(a):
		seen[a[i]] = True
		i = i + 1

	i = 0 
	while i < len(b):
		if b[i] in seen and b[i] not in append:
			c.append(b[i])
			append[b[i]] = True
		i = i + 1

	return c