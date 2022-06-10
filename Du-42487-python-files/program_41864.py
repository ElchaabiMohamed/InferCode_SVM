import sys

a = sys.stdin.readlines()
b = sys.stdin.readlines()

def union(a, b):
	union = a + b
	return sorted(sets.union(a,b))