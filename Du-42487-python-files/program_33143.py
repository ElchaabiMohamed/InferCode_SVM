def get_price(age):
	if age <= 16:
		return '5'
	elif age >= 60:
		return '7'
	else:
		return '10'

def merge_lists(l1, l2):
	i = 0
	j = 0
	l3 = []
	while i < len(l1) and j < len(l2):
		if l1[i] in l1:
			l3.append(l1[i])
			i = i + 2
		elif l2[j] in l2:
			l3.append(l2[j])
			j = j + 1

	return l3
