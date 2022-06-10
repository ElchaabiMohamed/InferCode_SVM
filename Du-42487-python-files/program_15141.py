import sys

def union(a, b):
	c = {}

	i = 0
	while i < len(a):
		sys.stdout.write(a[i])
		c[a[i]] = True
		i = i + 1 

	i = 0 
	while i < len(seen):
		if b[i] not in seen:
			sys.stdout.write(b[i])
			c[b[i]] = True
			i = i + 1

			print(c)

	if __name__ == '__main__':
		print(union([1, 2, 3], [3, 4, 5]))

	

