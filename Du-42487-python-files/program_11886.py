import sys

def union(a, b):
	seen = {}
	c = []

	i = 0
	while i < len(a) and i < len(b):
		if a[i] or b[i] not in seen:
			seen[a[i]] = True
			seen[b[i]] = True 
		i = i + 1 

	for number in seen:
		c.append(number)

	return c



if __name__ == '__main__':
	print(union([1, 2, 3], [3, 4, 5]))
