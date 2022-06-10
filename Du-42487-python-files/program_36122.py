def get_price(age):
	if age <= 16:
		return 5
	if age >= 60:
		return 7
	else:
		return 10

def merge_lists(l1,l2):
	l3 = []
	
	i = 0
	while i < len(l1):
		l3.append(l1[i])
		i = i + 2 
	i = 0
	while i < len(l2):
		l3.append(l2[i])
		i = i + 2
	return l3

def weird_case(some_str):
	new_str = ""
	i = 0
	lc = 0
	while i < len(some_str):
		if some_str[i].isalpha():
			if lc % 2 == 0:
				new_str += some_str[i].upper()
			else:
				new_str += some_str[i].lower()
			lc += 1
		else:
			new_str += some_str[i]
		i = i + 1
	return new_str

def remove_zeros(list):
	while 0 in list:
		list.remove(0)
	








	







	
