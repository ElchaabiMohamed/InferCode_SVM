#!/usr/bin/env python3

import sys

def swap_key_values(d):
	new_d = {}
	mylist = list(d.items())
	i = 0
	while i < len(mylist):
		d_key = mylist[i][0]
		d_val = mylist[i][1]
		new_d[d_val] = d_key
		i += 1
	return new_d



