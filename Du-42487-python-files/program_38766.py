#!/usr/bin/env python3

import sys

def swap_keys_values(dictionary):
	oldkeys = []
	oldvalues = []
	swappeddict = {}
	for key in dictionary:
		oldkeys.append(list(dictionary.keys()))
		oldvalues.append(list(dictionary.values()))

	for e in oldkeys:
		swappeddict[oldvalues] = oldkeys

	return swappeddict