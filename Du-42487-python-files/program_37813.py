#!/usr/bin/env python
import sys

def swap_keys_values(d):
	dic = {}
	for k, v in list(d.items()):
		dic[v] = k 
	return dic	