
i = 1
while i <101:
  if i % 3 == 0:
    print('fizz')
  elif i % 5 == 0:
    print('buzz')
  elif i % 3 == 0 and n % 5 == 0:
    print('fizzbuzz')
  else:
    print(i)
  i = i + 1
