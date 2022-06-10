a=int(input())
i=0
while i <= 100:
	if a % 3 == 0:
		print("Fizz")
	elif a % 5 == 0:
		print("Buzz")
	elif a % 3 == 0 and a % 5 == 0:
		print("FizzBuzz")
	else:
		print(a)