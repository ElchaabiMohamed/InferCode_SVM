import sys

def minimum(l):
	if len(l) == 0:
		return l[0]
	min = minimum(l[1:])
	if l[0] < min:
		return l[0]
	else:
		return min