#!/usr/bin/env python

def sumup(number):

    if number == 0:
        return 0

    return sumup(number- 1) + number 
