def get_price(age):
	if age <=16:
		get_price == 5.00
	elif age >= 60:
		get_price == 7.00
	else:
		get_price == 10


if __name__ == '__main__':
   print('calling get_price(\'age\')')
   print(get_price('age'))