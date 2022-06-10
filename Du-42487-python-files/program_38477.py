
def get_price(age):
	if age <= 16:
		return '5'
	if age > 60:
		return '7'
	else:
		return '10'

def merge_lists(l1,l2):
	i = 0
	mergedlist = []
	while i < len(l1):
		mergedlist.append(l1[i])
		i = i + 2
	j = 0
	while i < len(l2):
		mergedlist.append(l2[j])
		j = j + 2
	return mergedlist

def weird_case(some_str):
	ret = ""
	i = True
	for char in some_str:
		if i:
			ret += char.upper()
		else:
			ret += char.lower()
		if char != ' ':
			i = not i
	return ret

def remove_zeros(list):
	i = 0
	while i < len(list):
		if 0 in list:
			list.remove(0)
		i = i + 1
	

