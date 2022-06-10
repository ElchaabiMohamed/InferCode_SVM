def get_price(age):
	if int(age) <= 16:
	 	return "5"
	elif int(age) > 60:
		return "7"
	else:
		return "10"
def merge_lists(l1,l2):
	a = []
	i = 0
	while i < len(l1):
		a.append(l1[i])
		i = i + 2
	j = 0
	while j < len(l2):
		a.append(l2[j])
		j = j + 2
	return a
def remove_zeros(a):
	i = 0
	while i < len(a):
		if a[i] == 0:
			del a[i]
		if a[i] == 0:
			del a[i]
		i = i + 1
	

