n = eval(input())
if int(n) % 3 == 0 and int(n) % 5 != 0:
	print('Fizz')
elif int(n) % 5 == 0 and int(n) % 3 != 0:
	print('Buzz')
elif int(n) % 5 == 0 and int(n) % 3 == 0:
	print('FizzBuzz')
