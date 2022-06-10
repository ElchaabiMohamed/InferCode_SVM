
j=1
while j<=100:
  if j%3==0 and j%5==0:
    print("FizzBuzz")
    j=j+1
  elif j%3==0:
    print("Fizz")
    j=j+1
  elif j%5==0: 
    print("Buzz")
    j=j+1
  else:
    print(j)
    j=j+1
