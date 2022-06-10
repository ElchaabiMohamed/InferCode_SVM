import sys

def union(a, b):
	seen = {}
	c = []

	i = 0
	while i < len(a):
		seen[a[i]] = True
		i = i + 1 

	i = 0 
	while i < len(seen):
		if b[i] not in seen:
			seen[b[i]] = True
			i = i + 1

	for c in seen:
		return c

if __name__ == '__main__':
	print(union([1, 2, 3], [3, 4, 5]))




