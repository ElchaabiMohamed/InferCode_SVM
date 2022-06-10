a=1
while a <= 100:
	if a % 3 == 0:
		print("fizz")
	elif a % 5 == 0:
		print("buzz")
	elif a % 3 == 0 or a % 5 == 0:
		print("fizzbuzz")
	else:
		print(a)
	a = a + 1