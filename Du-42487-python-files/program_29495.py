#!/bin/usr/env python

def get_price(age):
	if age < 17:
		return "5"
	elif age > 60:
		return "7"
	else:
		return "10"

def merge_lists(l1,l2):
	l3 = l1[::2] + l2[::2]
	return l3

#def werid_case(some_str):


def remove_zeros(list):
	i = 0
	while i < len(list):
		if int(list[i]) == 0:
			list.remove(list[i])
		i = i + 1