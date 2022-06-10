#!/usr/bin/env python

def reverse_list(l = []):
	if len(l) == 0:
		return l
	x = []
	for i in reversed(l):
		x.append(i)
	return x

