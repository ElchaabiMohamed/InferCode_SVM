#!/usr/bin/env python

def minimum(l = []):
	if len(l) == 0:
		return l
	lowest = 0
	i = 0
	while i < len(l):
		if i > lowest:
			lowest = i
	return lowest