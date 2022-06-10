import sys

def union(a, b):
	c = {}

	i = 0
	while i < len(a):
		c[a[i]] = True
		i = i + 1 

	i = 0 
	while i < len(seen):
		if b[i] not in seen:
			c[b[i]] = True
			i = i + 1

	return c

if __name__ == '__main__':
	print(union([1, 2, 3], [3, 4, 5]))




