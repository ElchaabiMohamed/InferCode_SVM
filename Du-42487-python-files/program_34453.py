i = 0
while i <= 100:
  if i % 3 == 0 and not(i%5==0):
    print("fizz")
  elif i % 3 == 0 and i% 5 == 0:
    print("fizzbuzz")
  elif i % 5 == 0 and not i% 3 ==0:
    print("buzz")
  else: 
    i = i + 1
    print(i)
   
