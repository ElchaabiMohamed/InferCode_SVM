#!/bin/usr/env python

def get_price(age):
	if age < 17:
		return "5"
	elif age > 60:
		return "7"
	else:
		return "10"

