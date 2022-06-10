#!/usr/bin/env python

import time

def countdown(num):
    i = 0
    x = num
    while i < 1:
        print(x)
        time.sleep(0.1)
        x = x - 1
        i = i + 1
    print("LIFT OFF")
