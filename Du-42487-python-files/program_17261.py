#!/usr/bin/env python

def get_price(age):
	if age < 17:
		return 5
	elif age < 60:
		return 7
	else:
		return 10

if __name__ == '__main__':
	print('calling get_price(16)')
	print(get_price(16))
	print('calling get_price(35)')
	print(get_price(35))   
	print('calling get_price(60)')    
	print(get_price(60))