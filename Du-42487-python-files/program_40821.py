inp = 1
while inp <= 100:
   if inp%3 and inp%5 == 0:
      print("fizzbuzz")
   elif inp%3 == 0:
      print("fizz")
   elif inp%5 == 0 :
      print("buzz")
   else:
      print(inp)
   inp = inp + 1

