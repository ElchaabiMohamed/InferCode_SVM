fb = 1
while (fb <= 100):
    if (fb % 5) == 0 and (fb % 3) == 0:
        print("fizzbuzz")
    elif (fb % 3) == 0:
        print("fizz")
    elif (fb % 5) == 0:
        print("buzz")
    else:
        print(fb)

    fb = fb + 1
