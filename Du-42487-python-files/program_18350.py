#!/usr/bin/env python

i = 1
while i < 101:
    if i % 5 == 0 and i % 3 == 0:
        print(str("fizzbuzz"))
    elif i % 3 == 0:
        print(str("fizz"))
    elif i % 5 == 0:
        print(str("buzz"))
    else:
        print(i)
    i = i + 1
