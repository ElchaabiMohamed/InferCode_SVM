#!/bin/usr/env python

def get_price(age):
	if age < 17:
		return "5"
	elif age > 60:
		return "7"
	else:
		return "10"

def merge_lists(l1,l2):
	i = 0
	l3 = []
	while i < len(l1):
		l3.append(l1[i])
		i = i + 2
	print(l3)