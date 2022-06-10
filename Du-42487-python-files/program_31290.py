x = eval(input())

if x%5 == 0 and x%3 ==0:
	print("Fizz-Buzz")
elif x%3 ==0:
	print("Fizz")
elif x%5 ==0:
	print("Buzz") 
else:
	print(x)