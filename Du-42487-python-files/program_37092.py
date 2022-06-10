#!/usr/bin/env python

def swap_keys_values(d):
	new_d = {}
	for key in d:
		if d[key] not in new_d:
			new_d[d[key]] = key
		else:
			del(new_d[key])
	return new_d