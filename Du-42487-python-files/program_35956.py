def union(a,b):
	c = []
	ab = a+b
	for i in ab:
		if not i in c:
			c.append(i)
	return c
	
def intersection(a,b):
	c = []
	for i in a:
		if i in a and i in b and not i in c:
			c.append(i)
	return c
