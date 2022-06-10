fb = 0
while (fb < 101):
    if (fb % 5) == 0 and (fb % 3) == 0:
        print("FizzBuzz")
        fb = fb +1
    elif (fb % 3) == 0:
        print("Fizz")
        fb = fb + 1
    elif (fb % 5) == 0:
        print("Buzz")
        fb = fb +1
    else:
        print(fb)
        fb = fb + 1
