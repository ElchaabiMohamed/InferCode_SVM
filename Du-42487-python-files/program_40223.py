#!/usr/bin/env python

import sys

def swap_unique_keys_values(d):
	unique = {}
	new_d = {}
	for key in d:
		if d[key] not in unique:
			unique[d[key]] = 0
		unique[d[key]] = unique[d[key]] + 1

	for key in d:
		if unique[d[key]] == 1:
			new_d[d[key]] = key

	return new_d

def main():
	my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
	print((swap_unique_keys_values(my_dict)))

if __name__ == '__main__':
	main()