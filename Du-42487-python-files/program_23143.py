import sys

def power(m, n):
	if n == 1 or n == 0:
		return m
	return m + (m ** power(n-1))