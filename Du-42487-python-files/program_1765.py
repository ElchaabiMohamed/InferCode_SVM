#!/usr/bin/env python3

def sumup(n):
	if n < 2:
		return n
	sum_to_n = sumup(n-1)
	return n + sum_to_n