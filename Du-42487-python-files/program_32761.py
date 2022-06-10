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

def weird_case(some_str):
	some_str_split = list(some_str)
	i = 0
	k = 0
	string = ""
	while i < len(some_str_split):
		if some_str_split[i].isalpha() == True:
			if k % 2 == 0:
				string = string + some_str_split[i].upper()
			else:
				string = string + some_str_split[i].lower()
			i = i + 1
		return string

def remove_zeros(list):
	i = 0
	while i < len(list):
		if int(list[i]) == 0:
			list.remove(list[i])
			list.remove(list[i])
		i = i + 1