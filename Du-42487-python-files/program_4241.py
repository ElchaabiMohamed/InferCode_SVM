def get_price(age):
	if int(age) <= 16:
		price =5 
	elif int(age) > 60:
		price = 7
	else:
		price = 10
	return price

def merge_lists(l1,l2):
	i = 0
	l3=[]
	while i < len(l1):
		l3.append(l1[i])
		i += 2
	j = 0
	while j < len(l2):
		l3.append(l2[i])
		j += 2
		return l3