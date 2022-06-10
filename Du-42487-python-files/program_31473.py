#!/usr/bin/env python
import sys
def union(a,b):
	result = a + b

	s = []
	i = 0
	line = result[i]
	while 0 < len(line):
		while i < len(a) and s[i] != line:
			i = i + 1
		if i == len(s):
			s.append(line)
	return result

if __name__ == '__main__':
	print(union(a,b))