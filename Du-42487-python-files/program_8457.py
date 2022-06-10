#!/usr/bin/env python3

def swap_keys_values(d):
	d_swap = {}
	for x in d:
		d_swap[d[x]] = x
	return d_swap

def swap_unique_keys_values(d):
	d_swap = {}
	d_tmp = {}
	for x in d:
		d_swap[d[x]] = x
	return d_swap
