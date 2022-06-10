#usr!/bin/env python
import time

def countdown(number):
    while number > 0:
        print(number)
        time.sleep(.1)
        number -= 1
        if number == 0:
            print("LIFT OFF!")	

def search(str,letter):
	if letter in str:
		return True
	else:
		return False

def index(str,letter):
	if letter not in str:
		return -1
	else:
		return letter.index()