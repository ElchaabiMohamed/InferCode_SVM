def get_price(n):
	if int(n) <= 16:
		return 5
	elif int(n) > 60:
		return 7
	else:
		return 10