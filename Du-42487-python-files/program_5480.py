#!/usr/bin/env python
import sys
def union(a,b):
	result = a + b

	s = []
	i = 0
	line = result[i]
	while i < len(a):
		seen [a[i]] = True
		while i < a and s[i] != line:
			i = i + 1
		if i == len(s):
			s.append(line)
	return 

if __name__ == '__main__':
	print(union(a,b))