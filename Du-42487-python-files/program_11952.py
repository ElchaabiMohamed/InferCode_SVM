number = eval(input())

i = 0
while i < 100:
	if number%3 ==0:
		print('Fizz')
	elif number%5 == 0:
		'Buzz'
	elif number%5 == 0 and number%3 == 0:
		print('FizzBuzz')
	else:
		print(number) 