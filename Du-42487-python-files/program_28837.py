a=1
while a <= 100:
	if a % 3 == 0:
		print("Fizz")
	elif a % 5 == 0:
		print("Buzz")
	elif a % 3 == 0 and a % 5 == 0:
		print("Fizzbuzz")
	else:
		print(a)
	a = a + 1