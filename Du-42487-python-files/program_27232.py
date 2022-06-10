#!usr/bin/env python
def get_price(age):
	if int(age) <= 16:
		price = 5
	elif int(age) > 60:
		price = 7
	else:
		price = 10
	return price

def merge_lists(l1,l2):
	i = 0
	while i < len(l1) and i < len(l2):
		l3 = l1[i] + l2[i]
		i += 2
		return l3