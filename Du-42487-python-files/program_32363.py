n = int(input("fizz buzz (1-100"))

if n % 3 == 0:
	print("Fizz")
elif n % 5 == 0:
	print("Buzz")
elif n % 3 == 0 and n % 5 == 0:
	print("Fizz-Buzz")