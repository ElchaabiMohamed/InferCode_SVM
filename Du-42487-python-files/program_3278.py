number = eval(input())
i = 1
while i < 100:
	if number % 5 == 0 and number % 3 == 0:
		print("FizzBuzz")
		i = i + 1
	elif number % 3 == 0:
		print("Fizz")
		i = i + 1
	elif number % 5 == 0:
		print("Buzz")
		i = i + 1
	else:
		print(number)
		i = i + 1
