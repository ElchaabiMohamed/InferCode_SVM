#!/bin/usr/env python

import time

def countdown(num):
	i = 0
	while i < len(num):
		print(n -i)
		time.sleep(0.1)
		i = i + 1
	print("LIFT OFF")

def search(str,letter):
	if letter in str:
		return True
	else:
		return False