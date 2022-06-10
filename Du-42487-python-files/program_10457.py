import sys

def minimum(l, min):
	if not l:
		return []

	return minimum(l[1:], l[0] if l[0] < val else val)