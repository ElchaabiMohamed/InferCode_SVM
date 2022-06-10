#function definition
def get_price(age):
	age = input()
	if age > 60:
		return over_sixties
	elif age <= 16:
		return sixteen_and_under
	else:
		return everyone_else
		
#age divisions
sixteen_and_under = 5
over_sixties = 7
everyone_else = 10