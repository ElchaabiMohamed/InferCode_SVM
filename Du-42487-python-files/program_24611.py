n = 1
while n <= 100:
	if n % 5 == 0 and n % 3 == 0:
		print("FizzBuzz")
	elif n % 5 == 0:
		print("Buzz")
	elif n % 3 == 0:
		print("Fizz")
	i = i + 1 