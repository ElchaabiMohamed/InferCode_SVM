def get_price(age):
	if age < 17:
		return 5
	elif age >= 60:
		return 7
	else:
		return 10

def merge_lists(l1,l2):
	return l1[0::2] + l2[0::2]
	
def weird_case(some_str):
	weird = []
	i = 0
	while i < len(some_str):
		if i%2==0:
			weird.append(some_str[i].upper())
		else:
			weird.append(some_str[i])
		i += 1
	return ''.join(weird)
	
def remove_zeros(list):
	for i in list:
		if i == 0:
			list.remove[i]	

if __name__ == '__main__':
   print('calling get_price(17)')
   print(get_price(17))
   print('calling get_price(35)')
   print(get_price(35))   
   print('calling get_price(60)')
   print(get_price(60))   
   
   print('calling merge_lists([3,4,5,6],[12,2,5])')
   print(merge_lists([3,4,5,6],[12,2,5]))
   
   print('calling weird_case(\'change the case\')')
   print(weird_case('change the case'))
   
