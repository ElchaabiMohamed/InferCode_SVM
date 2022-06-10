#!/usr/bin/env python

def minimum(l = []):
	if len(l) == 0:
		return l
	lowest = 0
	for i in range(1, len(l)):
		if i > lowest:
			lowest = i
	return lowest