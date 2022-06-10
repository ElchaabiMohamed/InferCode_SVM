import sys

def minimum(l, n=0):

	min = minimum(l[1:], n-1)
	if l[0] < min:
		return l[0]
	else:
		return min