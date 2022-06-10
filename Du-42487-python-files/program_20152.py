number=100
i=1
while i < number + 1:
	if i % 3 == 0 and i % 5 == 0:
		print("fizzbuzz")
	elif i % 3 == 0:
		print("fizz")
	elif i % 5 == 0:
		print("buzz")
	else:
		print(i)
	i=i+1