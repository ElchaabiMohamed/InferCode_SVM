counter = 1
while counter != 101:
 if counter % 3 == 0:
  print("fizz")
 if counter % 5 == 0:
  print("buzz")
 if counter % 3 ==0 and counter % 5 == 0:
  print("fizzbuzz")
 print(counter)
 counter += 1
