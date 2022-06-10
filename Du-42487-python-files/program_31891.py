import sys 

def get_price(age):
	age = eval(input())
	if int(age) < 16:
		print("you pay 5 euro")
	elif int(age) > 60:
		print("you pay 7 euro")
	else:
		print("you pay 10 euro")