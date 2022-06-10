import sys

def union(a, b):
	seen = {}

	i = 0
	while i < len(a):
		sys.stdout.write(a[i])
		seen[a[i]] = True
		i = i + 1 

	i = 0 
	while i < len(seen):
		if b[i] not in seen:
			sys.stdout.write(b[i])
			seen[b[i]] = True
			i = i + 1
	for list in seen:
		print(list)

	if __name__ == '__main__':
		print(union([1, 2, 3], [3, 4, 5]))

	

