def get_price(age):
	if age <=16:
		return 5
	elif age >= 60:
		return 7
	else:
		return 10


def merge_lists(l1,l2):
	l3 = l1[::2] + l2[::2]
	return l3[::2]
	#l3 = []
	#for i in l1:
	#	l3 = l3 + [i[::l2]]
	#return l3
	#for num in l1:
	#	l3.append(num)
	#for number in l2:
	#	l3.append(number)
	#sorted(l3)
	#return l3

	#l3 = l1 + l2
	#return l3

if __name__ == '__main__':
   print('calling merge_lists(\'l3\')')
   print(merge_lists('l3'))