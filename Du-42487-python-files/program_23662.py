import sys

def get_price(age):
	if age >= 16:
		age_cost = 5
	elif age > 60:
		age_cost = 7
	else:
		age_cost = 10
	return age_cost
	
print(age_cost)