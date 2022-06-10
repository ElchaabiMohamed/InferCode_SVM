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

def weird_case(some_str):
	i = 0
	ls = []
	while i < len(some_str):
		if i % 2 == 0:
			ls.append(some_str[i].upper())
		else:
			ls.append(some_str[i].lower())
		i = i + 1
	return ''.join(ls)