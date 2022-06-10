
counter = 1
while counter <= 100:
	if counter % 5 == 0:
		print('Fizz')
	elif counter % 3 == 0:
		print('Buzz')
	elif counter % 5 == 0 and counter % 3 == 0:
		print('FizzBuzz')
	counter = counter + 1