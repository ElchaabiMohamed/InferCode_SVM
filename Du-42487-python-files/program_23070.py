import sys

def sumup(n):
	if n == 0:
		return 0
	return sumup(n + (n-1))