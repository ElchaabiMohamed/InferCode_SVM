#!/usr/bin/env python

def union(a,b):

	seen = []
	i = 0
	while i < len(a):
		seen[a[i]] = True
		i = i + 1

	j = 0
	while j < len(b):
		if (b[k] not in b):
			seen[b[k]] = True
		j = j + 1

	return 

if __name__ == '__main__':
	print(union(a,b))