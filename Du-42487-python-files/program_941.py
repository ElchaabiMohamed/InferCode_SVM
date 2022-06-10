#!/usr/bin/env python

i = 0
while i < 101:
    if i % 3 == 0:
        print(str("Fizz"))
    if i % 5 == 0:
        print(str("Buzz"))
    if i % 5 == 0 and i % 3 == 0:
        print(str("FizzBuzz"))
    else:
        print(i)
    i = i + 1
