#!/usr/bin/env python 

def factorical(n):
	if n == 0:
		return 0
	return n * factorical(n - 1)