a=int(input())
i=0
while i <= 100:
	if a[i] % 3 == 0:
		print("Fizz")
	elif a[i] % 5 == 0:
		print("Buzz")
	elif a[i] % 3 == 0 and a[i] % 5 == 0:
		print("FizzBuzz")