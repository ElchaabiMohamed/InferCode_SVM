#!/usr/bin/env python

def minimum(l = []):
	if len(l) == 0:
		return l
	lowest = 0
	for i in l:
		if i > lowest:
			i = lowest
	return lowest