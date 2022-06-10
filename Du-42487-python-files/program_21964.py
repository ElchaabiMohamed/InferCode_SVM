#!/usr/bin/env python3

import sys

def swap_keys_values(dictionary):
	oldkeys = []
	oldvalues = []
	invalid = []
	swappeddict = {}
	for value in list(dictionary.values()):
		if value not in oldvalues:
			oldvalues.append(value)
		else:
			oldvalues.pop(value)
			invalid.append(value)

	for key in list(dictionary.keys()):
		if key.value() not in invalid:
			oldkeys.append(key)


	i = 0
	while i < len(oldkeys):
		swappeddict[oldvalues[i]] = oldkeys[i]
		i = i + 1

	return swappeddict
