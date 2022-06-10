import sys

def get_price(age):
	if int(age) <= 16:
	 	return "5"
	elif int(age) > 60:
		return "7"
	else:
		return "10"
