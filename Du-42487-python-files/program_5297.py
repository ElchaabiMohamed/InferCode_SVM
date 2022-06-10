import sys

def get_price(age):
	age_cost = 0
	if age <= 16:
		age_cost = 5
	elif age > 60:
		age_cost = 7
	else:
		age_cost = 10
	return age_cost

def merge_lists(l1,l2):
	k = 0
	l3 = []
	while k < len(l1):
		l3.append(l1[k])
		k = k + 2
	k = 0
	while k < len(l2):
		l3.append(l2[k])
		k = k + 2
		
	return l3
	
def weird_case(some_str):
	some_str_split = list(some_str)
	i = 0
	k = 0 ## k is used as a count of the alpha characters so spaces are not capitalised.
	string = ""
	while i < len(some_str_split):
		if some_str_split[i].isalpha() == True:
			if k % 2 == 0:
				string = string + some_str_split[i].upper()
			else:
				string = string + some_str_split[i].lower()
			k = k + 1
		else:
			string = string + some_str_split[i]
		i = i + 1
	return string
	
def remove_zeros(list):
	print(list)
		