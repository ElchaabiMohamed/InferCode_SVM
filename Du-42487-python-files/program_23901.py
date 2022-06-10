#!/usr/bin/env python3

import sys

def swap_unique_keys_values(dictionary):
	oldkeys = []
	oldvalues = []
	swappeddict = {}
	for value in list(dictionary.values()):
		oldvalues.append(value)

	for key in list(dictionary.keys()):
		oldkeys.append(key)

	i = 0
	while i < len(oldkeys):
		swappeddict[oldvalues[i]] = oldkeys[i]
		i = i + 1

	for value in oldvalues:
		if oldvalues.count(value) == 2 and value in swappeddict:
			swappeddict.pop(value)

	return swappeddict
