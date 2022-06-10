import sys

def power(m, n):
	if n == 1 or n == 0:
		return m
	elif m == 1:
		return m
	elif m == 0:
		return 0

	return m + power(m, n-1)