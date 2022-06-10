i = 0
while i < 100:
   if i % 3 == i % 5:
      print("FizzBuzz")
   elif i % 3:
      print("Fizz")
   elif i % 5:
      print("Buzz")
   else:
      print(i)
   i = i + 1