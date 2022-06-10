def get_price(age):
	if age < 17:
		print("5")
	elif age > 60:
		print("7")
	else:
		print("10")



#def merge_lists(l1,l2):

#def weird_case(some_str):

def remove_zeroes(list):
	return [value for value in list if value != 0]

	
if __name__ == '__main__':
   print('calling get_price(\'change\')')