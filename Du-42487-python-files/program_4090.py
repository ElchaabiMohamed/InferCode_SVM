#usr!/bin/env python
import time

def countdown_numbers(number):
    while number > 0:
        print(number)
        number += 1
        if number == 0:
            print("LIFT OFF!")	
