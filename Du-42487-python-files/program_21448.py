n = 1
while i <=100:
  if n % 3 == 0:
    print("Fizz")
  elif n % 5 == 0:
    print("Buzz")
  elif n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
  else:
    print(n)
  n = n + 1
