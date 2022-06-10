def get_price(age):
	if age < 17:
		return 5
	elif age > 60:
		return 7
	else:
		return 10
		
def merge_lists(l1, l2):
	l3 = l1 + l2
	l4 = []
	i = 0
	while i < len(l3):
		l4.append(l3[i])
		i = i + 2
	return l4

def weird_case(some_str):
	i = 0
	while i < len(some_str):
		some_str[i].upper()
		i = i + 2
	return some_str
	
