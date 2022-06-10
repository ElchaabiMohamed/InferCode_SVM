def get_price(age):
	if age <=16:
		return 5
	elif age >= 60:
		return 7
	else:
		return 10

def merge_lists(l1,l2):
	l3 = l1 + l2

if __name__ == '__main__':
   print('calling merge_lists(\'l1,l2\')')
   print(merge_lists('l1,l2'))