#!/usr/bin/env python3

def swap_keys_values(d):
	d_swap = {}
	for x in d:
		d_swap[d[x]] = x
	return d_swap

def swap_unique_keys_values(d):
	d_swap = {}
	for x in d:
		if d[x] in d_swap:
			del d_swap[d[x]]
		else:
			d_swap[d[x]] = x
	return d_swap
