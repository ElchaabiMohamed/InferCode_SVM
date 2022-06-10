import sys

def reverse(l):
	if len(l) == 0:
		return []

	return l[-1] + rev(l[:-1])