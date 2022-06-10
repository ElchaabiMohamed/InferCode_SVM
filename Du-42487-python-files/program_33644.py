import sys

def factorial(m, n):
	if n == 1 or n == 0:
		return m
	return m + (m ** factorial(n-1))