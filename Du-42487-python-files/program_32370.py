import sys 

def get_price(age):
	age = eval(input())
	if int(age) < 16:
		print("5")
	elif int(age) > 60:
		print("7")
	else:
		print("10")