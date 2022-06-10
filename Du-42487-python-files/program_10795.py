#!usr/bin/env python

num = 0
while num < 101:
    if num % 5 == 0 and num % 3 == 0 :
        print("FizzBuzz")
        num += 1
    elif num % 3 == 0:
        print("Fizz")
        num += 1
    elif num % 5 == 0 :
        print("Buzz")
        num += 1
    else:
        print(num)
        num += 1
