#!/bin/usr/env python

def get_price(age):
	if age < 17:
		return "5"
	elif age > 60:
		return "7"
	else:
		return "10"

def merge_lists(l1l2):
	l3 = l1[::2] + l2[::2]
	return l3