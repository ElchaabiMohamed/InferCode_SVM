def get_price(age):
	if int(age) <= 16:
	 	return "5"
	elif int(age) > 60:
		return "7"
	else:
		return "10"
def merge_lists(l1,l2):
	i = 1
	while i < len(l1):
		del l1[i]
	i = i + 1
	j = 1
	while i < len(l2):
		del l2[j]
	j = j + 1
	return l1 + l2




