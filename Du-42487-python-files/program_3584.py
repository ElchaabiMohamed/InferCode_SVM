
counter = 1
while counter <= 100:
	if counter % 5 == 0:
		print(counter,'Fizz')
	elif counter % 3 == 0:
		print(counter,'Buzz')
	elif counter % 5 == 0 and counter % 3 == 0:
		print(counter,'FizzBuzz')
	counter = counter + 1