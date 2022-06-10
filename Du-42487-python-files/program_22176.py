def get_price(age):
	if int(age) <= 16:
		return 5
	elif int(age) >= 60:
		return 7
	else:
		return 10

if __name__ == '__main__':
	print('calling get_price(age)')
	print(get_price(18))


def merge_lists(l1, l2):
	l3 = []
	i = 0
	while i < len(l1):
		l3.append(l1[i])
		i = i + 2

	j = 0
	while j < len(l2):
		l3.append(l2[j])
		j = j + 2

	return l3

if __name__ == '__main__':
	print('calling merge_lists(l1, l2)')
	print(merge_lists([3,4,5,6], [12,2,5]))


def weird_case(some_str):
	new_str=''
	i = 0
	while i < len(some_str):
		some_str = some_str[i].split().upper()
		if i == 0 or i % 2 == 0:
			new_str = new_str + some_str#.upper()
		else: 
			new_str = new_str + some_str#.lower()
		i = i + 1

#	j = 1
#	while j < len(some_str):
#		if some_str[j].isalpha():
#			some_str[j].lower()
#		j = j + 2

	return new_str

if __name__ == '__main__':
	print('calling weird_case(\'change the case\')')
	print(weird_case('change the case'))


def remove_zeros(list):
	i = 0 
	while i < len(list):
		if 0 in list:
			list.remove(0)
		i = i + 1

if __name__ == '__main__':
	print('calling remove_zeros(list)')
	print(remove_zeros([1,5,0,2,0,3]))