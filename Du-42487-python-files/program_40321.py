#!/bin/usr/env python

def get_price(age):
	if age < 17:
		return "pay 5 euro"
	elif age > 60:
		return "pay 7 euro"
	else:
		return "pay 10 euro"

