#!/usr/bin/env python

def minimum(l = []):
	if len(l) == 0:
		return l
	lowest = 0
	i = 0
	j = i + 1
	while i < len(l):
		if i < j[i]:
			j[i] = i

	return i