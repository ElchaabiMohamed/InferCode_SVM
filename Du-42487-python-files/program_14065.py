#function definition
def get_price(age):
	age = int(raw_input)
	if age > 60:
		return str(over_sixties)
	elif age <= 16:
		return str(sixteen_and_under)	
	else:
		return str(everyone_else)
		
#age divisions
sixteen_and_under = 5
over_sixties = 7
everyone_else = 10