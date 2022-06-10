#!/usr/bin/env python3

import sys

def swap_keys_values(dictionary):
	oldkeys = []
	oldvalues = []
	swappeddict = {}
	for key in list(dictionary.keys()):
		oldkeys.append(key)
	for value in list(dictionary.values()):
		oldvalues.append(value)


	i = 0
	while i < len(oldkeys):
		swappeddict[oldvalues[i]] = oldkeys[i]
		i = i + 1

	return swappeddict
