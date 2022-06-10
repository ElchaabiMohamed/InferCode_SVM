
counter = 1
while counter <= 100:
	if counter % 5 == 0 and counter % 3 == 0:
		print('fizzBuzz')
	elif counter % 5 == 0:
		print('buzz')
	elif counter % 3 == 0:
		print('fizz')
	
	else:
		print(counter)
	counter = counter + 1