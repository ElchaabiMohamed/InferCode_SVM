for numbers in range(1, 100):
   if  numbers % 3 == 0:
      print('fizz')
   elif numbers % 5 == 0:
      print('buzz')
   elif numbers % 15 == 0:
      print('fizzbuzz')
   else:
      print(numbers)