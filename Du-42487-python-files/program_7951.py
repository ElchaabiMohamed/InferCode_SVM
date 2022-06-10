#!/usr/bin/env python
import time
def countdown(num):

    i = 0
    x = num
    while i < num:
        print(x) 
        time.sleep(0.1)
        x = x - 1
        i = i + 1


def search(str,letter):
    for item in str:
        if item == letter:
            return True
    return False

#def index(str,letter):


#def fibonacci(n):






