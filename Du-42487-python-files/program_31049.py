import sys 

def get_price(age):
	 
	if int(age) < 16:
		return "5"
	elif int(age) > 60:
		return "7"
	else:
		return "10"


def merge_lists(l1,l2):
	i = 0
	while i < len(l2):
		l1.append(l2[i])
		i = i + 1

	i = 0
	while i < len(l1):
		if i % 2 == 1 and i != 0:
			l1.remove(l1[i])
		i = i + 1
	return l1	

		
def weird_case(some_str):
	import sys
	upper_list = ()
	some_str = sys.stdin.readline()
	letters = some_str.strip("\n").split(" ")
	i = 0
	while i < len(letters):
		if i % 2 == 1 and i != 0:
			letters[i].upper()
		i = 1 + i
	upper_list.append(letters)
	return upper_list

