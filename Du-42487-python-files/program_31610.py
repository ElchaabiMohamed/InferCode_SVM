def get_price(age):
	if int(age) <= 16:
		price =5 
	elif int(age) > 60:
		price = 7
	else:
		price = 10
	return price