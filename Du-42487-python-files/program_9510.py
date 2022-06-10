import sys

def minimum(l):
	min = None
	if not l:
		return []

	return minimum(l[-1] if l[-1] < min else min)