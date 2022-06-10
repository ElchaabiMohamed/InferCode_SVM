import sys
lines = sys.stdin.readlines()
n = lines

if n % 3 == 0 and n % 5 == 0:
	print("FizzBuzz")
elif i % 3 == 0:
	print("Fizz")
elif i % 5 == 0:
	print("Buzz")
else:
	print(n) 