import sys

def minimum(l):
	if not l:
		return []

	return minimum(min(l))