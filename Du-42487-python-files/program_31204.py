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
		l3.append(l2[j])
		j += 2
		return l3

def weird_case(some_str):
	i = 0 
	string2 = ""
	while i < len(some_str):
		some_str = str(some_str).split()
		print(some_str)
		i += 2
		return string2