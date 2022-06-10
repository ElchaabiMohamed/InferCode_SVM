#usr!/bin/env python
import time

def countdown(number):
    while number > 0:
        print(number)
        time.sleep(.1)
        number -= 1
        if number == 0:
            print("LIFT OFF!")	
