x = 1

while x <= 100:
	if x % 5 == 0 and x % 3 == 0:
		print("fizzbuzz")
		x = x + 1
	elif x % 5 == 0 and x % 3 != 0:
		print("buzz")
		x = x + 1
	elif x % 3 == 0 and x % 5 != 0:
		print("fizz")
		x = x + 1
	else:
		print(x)
		x = x + 1