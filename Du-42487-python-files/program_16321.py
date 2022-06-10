#!/bin/usr/env python

import time

def countdown(num):
	i = 0
	while i < num:
		print(num - i)
		time.sleep(0.1)
		i = i + 1
	print("LIFT OFF!")

def search(str,letter):
	if letter in str:
		return True
	else:
		return False

def index(str,letter):
	if letter in str:
		return str[0]
	else:
		return str[-1]