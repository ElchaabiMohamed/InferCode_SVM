#!/usr/bin/env python

import sys

def swap_keys_values(d):
	new_d = {}

	for key in d:
		new_d[d[key]] = key

	return new_d

def main():
	my_dict = {'a' : 4, 'b' : 7, 'c' : 10}
	print((swap_keys_values(my_dict)))

if __name__ == '__main__':
	main()