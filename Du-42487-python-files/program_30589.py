def get_price(age):
	return 5 if age < 17 else 7 if age >= 60 else 10

def merge_lists(l1,l2):
	return l1[0::2] + l2[0::2]
	
def weird_case(some_str):
    weird, i = [], True
    for char in some_str:
        weird += char.upper() if i else char
        if char != ' ':
            i = not i
    return ''.join(weird)
	
def remove_zeros(list):
	while 0 in list:
		for i in list:
			if i == 0:
				list.remove(i)	
	return list