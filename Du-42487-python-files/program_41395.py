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
	while k < len(l1):
		l3.append(l1[k])
		print(i, k)
		i = i + 1
		k = k + 2

	