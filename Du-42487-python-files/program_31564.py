#!/usr/bin/env python

def get_price(age):
	if age < 17:
		return 5
	elif age > 60:
		return 7
	else:
		return 10

def merge_lists(l1,l2):
	a = l1[0::2]
	b = l2[0::2]
	return a + b




