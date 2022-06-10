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

def remove_zeros(list):
	i = 0
	while i < len(list):
		if list[i] == 0:
			del list[i]
		else:
			i = i + 1
	return list

if __name__ == '__main__':
	print('calling remove_zeros([0,0,9])')
	print(remove_zeros([0,0,9]))

