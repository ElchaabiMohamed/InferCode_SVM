#!/usr/bin/env python3

import sys

def swap_keys_values(dictionary):
	oldkeys = []
	oldvalues = []
	swappeddict = {}
	for key in dictionary:
		oldkeys.append(list(dictionary.keys()))
		oldvalues.append(list(dictionary.values()))

	i = 0
	while i < len(oldkeys):
		swappeddict[oldvalues[i]] = oldkeys[i]
		i = i + 1

	return swappeddict