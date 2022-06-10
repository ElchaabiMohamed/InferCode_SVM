number = int(input())

counter = 1
while counter <= 100:
	if number % 5 == 0:
		print('Fizz')
	elif number % 3 == 0:
		print('Buzz')
	elif number % 5 == 0 and number % 3 == 0:
		print('FizzBuzz')
counter = counter + 1