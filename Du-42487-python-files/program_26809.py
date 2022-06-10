#!/usr/bin/env python3

import sys

def swap_keys_values(d):
	new_d = {}
	val_count = {}
	mylist = list(d.items())
	i = 0
	while i < len(mylist):
		d_key = mylist[i][0]
		d_val = mylist[i][1]
		if d_val not in val_count:
			val_count[d_val] = 1
			new_d[d_val] = d_key
		else:
			val_count[d_val] = 1
			del new_d[d_val]
		i += 1
	return new_d