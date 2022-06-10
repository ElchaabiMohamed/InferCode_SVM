import sys

def get_price(age):
	if int(age) <= 16:
	 	return "5 euro"
	elif int(age) > 60:
		return "7 euro"
	else:
		return "10 euro"
