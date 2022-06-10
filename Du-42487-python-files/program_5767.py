x = 100

while x <= 100:
	if x % 5 == 0 and x % 3 == 0:
		print("fizz-buzz")
	elif x % 5 == 0:
		print("buzz")
	elif x % 3 == 0:
		print("fizz")
	else:
		print(x)