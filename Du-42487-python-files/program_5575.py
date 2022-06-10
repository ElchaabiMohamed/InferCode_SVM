def get_price(age):
	age = int(age)
	if age <= 16:
		print('5')
	elif age >= 60:
		print('7')
	else:
		print('10')

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





