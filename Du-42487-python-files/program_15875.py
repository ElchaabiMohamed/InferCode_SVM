#!/usr/bin/env python3

def reverse_list(l):
	if len(l) == 1:
		return l

	new_l = reverse_list(l[1:]) + l[:1]
	return new_l
