def get_price(age):
	if int(age) <= 16:
	 	return "5"
	elif int(age) > 60:
		return "7"
	else:
		return "10"
def merge_lists(l1,l2):
	l3 = l1  + l2
	a = []
	i = 0
	while i < len(l3):
		a.append(l3[i])
		i = i + 2
	return a

