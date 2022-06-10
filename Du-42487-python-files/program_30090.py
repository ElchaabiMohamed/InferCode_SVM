def get_price(age):
	age = int(age)
	if age <= 16:
		return '5'
	elif age >= 60:
		return '7'
	else:
		return '10'

def merge_lists(l1,l2):
	list = []

	i = 0
	while i < len(l1):
		list.append(l1[i])
		i = i + 2

	i = 0
	while i < len(l2):
		list.append(l2[i])
		i = i + 2

	return list

def weird_case(some_str):
	some_str = str(some_str)

	i = 0
	while i < len(some_str):
		some_str = some_str.uppercase()
		i = i + 2
	return some_str





