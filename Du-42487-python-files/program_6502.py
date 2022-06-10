#!/usr/bin/env python
import sys

def swap_unique_keys_values(d):
	dic = {}
	for k, v in list(d.items()):
		if v not in dic:
			dic[v] = k 
		else:
			del dic[v]
	return dic