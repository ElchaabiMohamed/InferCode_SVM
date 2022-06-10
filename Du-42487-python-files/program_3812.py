def union(a, b, c):
	i = 0
	while i < len(a):
		c.append(a[i])
		i = i + 1

	p = 0
	while p < len(b):
		if b[p] not in c:
			c.append(b[p])
		p = p + 1

	return c

def intersection(a, b, d):
	i = 0
	while i < len(a):
		if a[i] in b:
			d.append(a[i])
		i = i + 1

	return d