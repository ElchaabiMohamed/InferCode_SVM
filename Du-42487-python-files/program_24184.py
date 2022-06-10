n = 100 
i = 0 

while i < n:
	i = i + 1

	if (i % 5) == 0 and (i % 3) == 0:
		print("FizzBuzz")

	elif i % 3 == 0:
		print("Fizz")

	elif i % 5 == 0:
		print("Buzz.")

	else:
		print(i) 