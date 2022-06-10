def get_price(age):
	age = input()
	if int(age) <= 16:
		return '5 euro'
	elif int(age) >= 60:
		return '7 euro'
	else:
		return '10 euro'

if __name__ == '__main__':
	print('calling get_price(age)')
	print(get_price())