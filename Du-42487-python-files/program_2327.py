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
	while i <= len(l1):
		l1_1 = l1[0:3]
		i += 2
		j = 0 
		while j < len(l2):
			l2_1 = l2[j]
			j += 2
			l3 = []
			l3.append(l1_1)
		return l3