import sys

age_cost = 0

def get_price(age):
	if age <= 16:
		age_cost = 5
	elif age > 60:
		age_cost = 7
	else:
		age_cost = 10
	return age_cost

def merge_lists(l1,l2):
	i = 0
	k = 0
	l3 = []
	while i < len(l1):
		l3.append(l1[k])
		if len(l1) > 2:
		   k = k + 2
	i = 0
	k = 0
	while i < len(l2):
		l3.append(l2[k])
		if len(l2) > 2:
		   k = k + 2
	