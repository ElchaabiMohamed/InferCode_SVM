#!/usr/bin/env python

def count_letters(s):
	total = 0
	if s == '':
		return 0
	for i in s:
		if s.isalpha():
			total += 1
	return total