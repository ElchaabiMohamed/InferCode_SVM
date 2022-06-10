#!usr/bin/env python

num = 0
while num < 101:
    if num % 5 == 0 and num % 3 == 0 :
        print("Fizz")
    elif num % 3 == 0:
        print("Buzz")
    elif num % 5 == 0 :
        print("FizzBuzz")
    else:
        print(num)
        num += 1
