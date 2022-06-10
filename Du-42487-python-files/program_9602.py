
i = 1
while i <= 100:
	if i % 3:
		print("Fizz")
	elif i % 5:
		print("Buzz.")
	elif i %3 and i %5:
		print("FizzBuzz.")
	else:
		print(i)
	i=i+1
