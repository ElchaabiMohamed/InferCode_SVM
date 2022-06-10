x = eval(input())

i = 0
while i <= 100:
	if x % 5 == 0 and x % 3 == 0:
		print("fizz-buzz")
		i = i + 1
	elif x % 5 == 0:
		print("buzz")
		i = i + 1
	elif x % 3 == 0:
		print("fizz")
		i = i + 1
	else:
		print(x)
		i = i + 1