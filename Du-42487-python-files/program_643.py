#!/usr/bin/env python

def reverse_list(l = []):
	if len(l) == 0:
		return l
	for i in reversed(l):
		return list(i)

