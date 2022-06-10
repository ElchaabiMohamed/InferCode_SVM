j = 1
while j <= 100:
  if j % 15 == 0:
    print("fizzbuzz")
  elif j % 5 == 0:
    print("buzz")
  elif j % 3 ==0:
    print("fizz")
  else:
    print(j)
  j = j + 1
