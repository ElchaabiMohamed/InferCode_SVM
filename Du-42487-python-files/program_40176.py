#!/usr/bin/env python

def union(a,b):
	result = a + b

	s = []
	i = 0
	while i < len(a):
		s[a[i]] = True
		i = i + 1

	if a[i] in s:
		s.append()


	return 

if __name__ == '__main__':
	print(union(a,b))