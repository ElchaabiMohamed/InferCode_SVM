import sys 

def get_price(age):
	 
	if int(age) < 16:
		print("5")
	elif int(age) > 60:
		print("7")
	else:
		print("10".rstrip("\n"))
